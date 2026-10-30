"""sound_scene1.py -- builds build/scene1_audio.wav for the 45.5 s scene 1 ink cut.

    python sound_scene1.py            # beds + voices -> amix -> loudnorm, then the checks
    python sound_scene1.py check      # re-print the level windows only

Ambience and effects are synthesised with numpy; the narration comes from audio/ and
the "settle" thock from the shared sfx palette.  Beds are written once, then ffmpeg
mixes them with the delayed voices (amix normalize=0) and normalises the result.
"""

import json
import os
import re
import subprocess
import sys
import wave

import numpy as np

import sfx

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
SR = 48000
DUR = 45.5
N = int(round(DUR * SR))

VOICES = [
    ("s1_suresh.mp3", 8.8),
    ("r1_ramesh.mp3", 13.8),
    ("s2_suresh.mp3", 24.8),
    ("r2_ramesh.mp3", 29.2),
    ("s3_suresh.mp3", 33.8),
]


# ------------------------------------------------------------------ helpers
def write_wav(path, x, sr=SR):
    x = np.clip(x, -1, 1)
    ch = x.shape[1] if x.ndim == 2 else 1
    with wave.open(path, "wb") as w:
        w.setnchannels(ch)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((x * 32767).astype("<i2").tobytes())


def read_wav(path):
    with wave.open(path, "rb") as w:
        sr, ch, n = w.getframerate(), w.getnchannels(), w.getnframes()
        raw = w.readframes(n)
    x = np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x, sr


def resample(x, src, dst=SR):
    if src == dst:
        return x
    n = int(round(len(x) * dst / src))
    return np.interp(np.arange(n) / dst, np.arange(len(x)) / src, x)


def fft_filter(x, lo=None, hi=None):
    """Smooth band-limit: gentle high-pass at lo, low-pass at hi (Hz)."""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.ones_like(f)
    if hi:
        g *= 1 / (1 + (f / hi) ** 4)
    if lo:
        g *= 1 - 1 / (1 + (f / lo) ** 4)
    return np.fft.irfft(X * g, len(x))


def _t(dur):
    return np.arange(int(round(dur * SR))) / SR


def _norm(x, peak=0.9):
    m = np.abs(x).max()
    return x / m * peak if m > 1e-9 else x


def _rms(x):
    return float(np.sqrt(np.mean(x ** 2)))


def _rms_norm(x, rms):
    m = _rms(x)
    return x * (rms / m) if m > 1e-9 else x


def _pink(n, seed):
    X = np.fft.rfft(np.random.default_rng(seed).standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR)
    return np.fft.irfft(X / np.sqrt(np.maximum(f, 20)), n)


def vramp(t, t0, t1):
    u = np.clip((np.asarray(t, float) - t0) / max(t1 - t0, 1e-9), 0, 1)
    return u * u * (3 - 2 * u)


# ------------------------------------------------------------------ stereo bus
class Bus:
    def __init__(self):
        self.x = np.zeros((N, 2))

    def add(self, sig, t0=0.0, gain=1.0, pan=0.0):
        i0 = int(round(t0 * SR))
        if i0 >= N:
            return
        if i0 < 0:
            sig = sig[-i0:]
            i0 = 0
        n = min(len(sig), N - i0)
        if n <= 0:
            return
        pan = float(np.clip(pan, -1, 1))
        gl = np.cos((pan + 1) * np.pi / 4)
        gr = np.sin((pan + 1) * np.pi / 4)
        self.x[i0:i0 + n, 0] += sig[:n] * gain * gl
        self.x[i0:i0 + n, 1] += sig[:n] * gain * gr


# ------------------------------------------------------------------ generators
def city_night(dur=3.5, seed=11):
    t = _t(dur)
    rumble = _rms_norm(fft_filter(_pink(len(t), seed), lo=30, hi=2200), 1.0)
    swell = 0.6 + 0.4 * np.sin(2 * np.pi * 0.25 * t + 0.5) ** 2
    air = fft_filter(np.random.default_rng(seed + 1).standard_normal(len(t)),
                     lo=1200, hi=4200) * 0.04
    env = np.clip(t / 0.7, 0, 1) * np.clip((dur - t) / 0.8, 0, 1)
    return (rumble * swell + air) * env


def engine_pass(dur=3.5, seed=12):
    t = _t(dur)
    u = t / dur
    f = 34 + 26 * np.sin(np.pi * u) ** 1.4
    ph = 2 * np.pi * np.cumsum(f) / SR
    tone = (np.sin(ph) + 0.55 * np.sin(2 * ph + 0.4)
            + 0.30 * np.sin(3 * ph + 1.0) + 0.15 * np.sin(4 * ph))
    noise = _rms_norm(fft_filter(np.random.default_rng(seed).standard_normal(len(t)),
                                 lo=60, hi=420), 1.0)
    env = np.sin(np.pi * u) ** 1.6
    return _norm((0.75 * _norm(tone, 1.0) + 0.35 * noise) * env, 0.9)


def horn():
    def honk(f0, dur=0.25):
        t = _t(dur)
        saw = 2 * ((f0 * t) % 1.0) - 1            # slightly nasal
        saw = fft_filter(saw, hi=1200)
        env = np.minimum(t / 0.01, 1) * np.minimum((dur - t) / 0.06, 1)
        return _norm(saw * env, 0.8)

    out = np.zeros(int(0.6 * SR))
    for i, f in ((0, 330.0), (int(0.35 * SR), 392.0)):
        a = honk(f)
        n = min(len(a), len(out) - i)
        out[i:i + n] += a[:n]
    return _norm(out, 0.85)


def engine_hum():
    t = np.arange(N) / SR
    brown = _rms_norm(fft_filter(np.cumsum(
        np.random.default_rng(3).standard_normal(N)), lo=20, hi=180), 1.0)
    stop = np.clip(vramp(t, 4.2, 4.45) - vramp(t, 7.6, 8.4), 0, 1)
    depth = 1 - stop                              # tremolo stops while the bus waits
    tone = np.sin(2 * np.pi * 52 * t) * (1 + 0.35 * depth * np.sin(2 * np.pi * 5 * t))
    gate = vramp(t, 3.4, 3.9) * (1 - vramp(t, 39.7, 40.05))
    level = (1 - 0.5 * stop) * gate
    return _rms_norm((0.8 * brown + 0.35 * tone) * level, 0.014)


def brake_hiss(dur=0.6, seed=5):
    t = _t(dur)
    x = fft_filter(np.random.default_rng(seed).standard_normal(len(t)),
                   lo=2500, hi=10000)
    env = np.minimum(t / 0.03, 1) * np.exp(-np.maximum(t - 0.04, 0) / 0.2)
    return _norm(x * env, 0.7)


def door_clank(seed=7):
    t = _t(0.25)
    out = np.zeros(len(t))
    for f0, a, d in ((380.0, 1.0, 0.05), (910.0, 0.6, 0.035), (1620.0, 0.35, 0.02)):
        out += a * np.sin(2 * np.pi * f0 * t) * np.exp(-t / d)
    click = fft_filter(np.random.default_rng(seed).standard_normal(len(t)),
                       lo=700, hi=4500)
    out += 0.6 * _norm(click, 1.0) * np.exp(-t / 0.008)
    return _norm(out * (1 - np.exp(-t / 0.001)), 0.8)


def footstep(seed):
    t = _t(0.14)
    thump = np.sin(2 * np.pi * 72 * t) * np.exp(-t / 0.045)
    scuff = fft_filter(np.random.default_rng(seed).standard_normal(len(t)),
                       lo=70, hi=400)
    scuff = _norm(scuff, 1.0) * np.exp(-t / 0.025)
    return _norm((0.8 * thump + 0.4 * scuff) * (1 - np.exp(-t / 0.002)), 0.85)


def pothole():
    t = _t(0.4)
    f = 42 + 60 * np.exp(-t / 0.12)
    thump = np.sin(2 * np.pi * np.cumsum(f) / SR)
    knock = _rms_norm(fft_filter(
        np.random.default_rng(9).standard_normal(len(t)), lo=40, hi=280), 1.0)
    env = (1 - np.exp(-t / 0.002)) * np.exp(-t / 0.11)
    return _norm((thump + 0.5 * knock) * env, 0.9)


def whoosh(dur=0.25, seed=6):
    t = _t(dur)
    u = t / dur
    noise = np.random.default_rng(seed).standard_normal(len(t))
    dark = _rms_norm(fft_filter(noise, lo=300, hi=900), 1.0)
    bright = _rms_norm(fft_filter(noise, lo=900, hi=5200), 1.0)
    x = (1 - u) * dark + u * bright            # rises as it swishes past
    return _norm(x * np.sin(np.pi * u) ** 1.5, 0.8)


def ka_ching():
    rng = np.random.default_rng(21)
    out = np.zeros(int(0.6 * SR))
    for i, f0 in enumerate((2093.0, 2637.0, 3136.0, 3951.0)):
        t = _t(0.6)
        env = (1 - np.exp(-t / 0.002)) * np.exp(-t / 0.16)
        y = (np.sin(2 * np.pi * f0 * t) + 0.30 * np.sin(2 * np.pi * 2.01 * f0 * t)
             + 0.15 * np.sin(2 * np.pi * 2.76 * f0 * t))
        s = int(i * 0.04 * SR)
        n = min(len(y), len(out) - s)
        out[s:s + n] += y[:n] * env[:n] * (0.9 - 0.15 * i)
    sparkle = fft_filter(rng.standard_normal(int(0.15 * SR)), lo=6000, hi=15000)
    sparkle = _norm(sparkle, 1.0) * np.exp(-np.arange(len(sparkle)) / SR / 0.05) * 0.2
    out[:len(sparkle)] += sparkle
    return _norm(out, 0.7)


def bubble_pop(dur=0.13):
    t = _t(dur)
    f = 90 + 700 * np.exp(-t / 0.022)
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.035)
    click = np.random.default_rng(4).standard_normal(len(t)) * np.exp(-t / 0.004) * 0.4
    return _norm(y + click, 0.7)


def bell_hit(f0, dur=0.8):
    t = _t(dur)
    y = np.zeros(len(t))
    for r, a, d in ((1.0, 1.0, 0.14), (2.0, 0.5, 0.09),
                    (2.76, 0.3, 0.06), (5.40, 0.15, 0.035)):
        y += a * np.sin(2 * np.pi * f0 * r * t) * np.exp(-t / d)
    y *= 1 - np.exp(-t / 0.0015)
    return _norm(y, 0.7)


def bus_bell():
    out = np.zeros(int(1.0 * SR))
    a, b = bell_hit(1318.5), bell_hit(1318.5)
    out[:len(a)] += a
    i = int(0.25 * SR)
    n = min(len(b), len(out) - i)
    out[i:i + n] += b[:n]
    return _norm(out, 0.75)


def crickets(dur=5.7, seed=31):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    out = np.zeros(n)
    t0 = 0.05
    while t0 < dur - 0.1:
        d = 0.05 + 0.02 * rng.random()
        m = int(d * SR)
        tt = np.arange(m) / SR
        e = np.sin(np.pi * tt / d) ** 2
        sig = np.sin(2 * np.pi * (4300 + 120 * rng.random()) * tt
                     + 0.6 * np.sin(2 * np.pi * 190 * tt)) * e
        i = int(t0 * SR)
        k = min(m, n - i)
        out[i:i + k] += sig[:k]
        t0 += 0.30 + 0.20 * rng.random()
    return _norm(out, 0.6)


def engine_pull(dur=3.7, seed=33):
    t = _t(dur)
    rumble = _rms_norm(fft_filter(np.cumsum(
        np.random.default_rng(seed).standard_normal(len(t))), lo=25, hi=150), 1.0)
    f = 48 - 10 * t / dur
    tone = _rms_norm(np.sin(2 * np.pi * np.cumsum(f) / SR), 1.0)
    u = t / dur
    env = np.clip(t / 0.08, 0, 1) * (1 - u) ** 1.4
    return _norm((0.8 * rumble + 0.5 * tone) * env, 0.9)


# ------------------------------------------------------------------ beds
def build_beds():
    os.makedirs(BUILD, exist_ok=True)
    bus = Bus()

    # 0.0-3.5 street at night: city bed, bus passing, horn
    bus.add(city_night(), 0.0, gain=0.0053)
    bus.add(engine_pass(), 0.0, gain=0.019, pan=-0.2)
    bus.add(horn(), 1.0, gain=0.049, pan=-0.2)

    # 3.5-39.8 inside the bus
    bus.add(engine_hum(), 0.0)
    bus.add(brake_hiss(), 3.9, gain=0.14, pan=0.05)
    bus.add(door_clank(), 4.4, gain=0.13, pan=-0.10)
    bus.add(footstep(13), 4.8, gain=0.07, pan=0.15)
    bus.add(footstep(14), 5.3, gain=0.07, pan=0.15)
    settle, sr = read_wav(str(sfx._file("settle")))
    bus.add(resample(settle, sr), 7.2, gain=0.16, pan=-0.05)

    bus.add(pothole(), 11.0, gain=0.18, pan=0.10)
    bus.add(whoosh(), 22.2, gain=0.11)
    bus.add(ka_ching(), 25.1, gain=0.15, pan=0.10)
    bus.add(bubble_pop(), 28.8, gain=0.09)
    bus.add(bus_bell(), 37.4, gain=0.22)

    # 39.8-45.5 bus stop outside: crickets, the bus pulling away on the right
    bus.add(crickets(), 39.8, gain=0.07, pan=0.45)
    bus.add(engine_pull(), 39.8, gain=0.05, pan=0.75)

    # fade everything out at the end of the shot
    t = np.arange(N) / SR
    bus.x *= (1 - vramp(t, 44.6, 45.5))[:, None]
    peak = np.abs(bus.x).max()
    if peak > 0.98:
        bus.x *= 0.98 / peak

    out = os.path.join(BUILD, "scene1_beds.wav")
    write_wav(out, bus.x)
    print("beds:", out, "rms %.1f dB" % (20 * np.log10(max(_rms(bus.x), 1e-9))))
    return out


# ------------------------------------------------------------------ mix
def build_audio():
    beds = build_beds()
    inputs = [beds] + [os.path.join(HERE, "audio", f) for f, _ in VOICES]

    chains = ["[0:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo[a0]"]
    for i, (_, start) in enumerate(VOICES, start=1):
        gl = gr = np.cos(np.pi / 4)                 # centred
        ms = int(round(start * 1000))
        # shave ~1.5 dB off the voice peaks so loudnorm can normalise linearly
        # (otherwise it falls back to dynamic mode and lifts the quiet ambience)
        chains.append(
            f"[{i}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=mono,"
            f"pan=stereo|c0={gl:.4f}*c0|c1={gr:.4f}*c0,"
            f"alimiter=limit=0.36:attack=2:release=80:level=false:latency=true,"
            f"adelay={ms}|{ms}[a{i}]")
    mix = ("".join(f"[a{i}]" for i in range(len(inputs)))
           + f"amix=inputs={len(inputs)}:normalize=0:duration=longest,"
             f"apad=whole_dur={DUR},atrim=0:{DUR}")
    graph = ";".join(chains) + ";" + mix
    cmd_in = sum([["-i", p] for p in inputs], [])
    # LRA wider than the mix's measured range keeps loudnorm in linear mode; the
    # default 11 would exceed it, fall back to dynamic, and lift the quiet ambience.
    ln = "loudnorm=I=-14:TP=-1.5:LRA=25"

    # pass 1: measure, so pass 2 can normalise linearly without moving the length
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *cmd_in,
                        "-filter_complex", graph + f",{ln}:print_format=json[o]",
                        "-map", "[o]", "-f", "null", "-"],
                       capture_output=True, text=True, check=True)
    m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S).group(0))
    ln2 = (f"{ln}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
           f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
           f"offset={m['target_offset']}:linear=true")

    out = os.path.join(BUILD, "scene1_audio.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *cmd_in,
                    "-filter_complex",
                    graph + f",{ln2},aresample=48000,atrim=0:{DUR}[o]", "-map", "[o]",
                    "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", out], check=True)
    print("audio:", out, "measured %.1f LUFS" % float(m["input_i"]))
    return out


# ------------------------------------------------------------------ checks
def check(path):
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", path],
                       capture_output=True, text=True, check=True).stdout.strip()
    print("duration: %s s" % d)
    for a, b in ((0, 3.5), (9, 13), (14, 24), (40, 44)):
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-ss", str(a),
                            "-to", str(b), "-i", path, "-af", "volumedetect",
                            "-f", "null", "-"], capture_output=True, text=True)
        mv = re.search(r"mean_volume:\s*(-?[\d.]+) dB", r.stderr)
        pv = re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr)
        print(f"  {a:>4}-{b:<3}s  mean {mv.group(1) if mv else '?':>6} dB"
              f"  max {pv.group(1) if pv else '?':>6} dB")


if __name__ == "__main__":
    wav = os.path.join(BUILD, "scene1_audio.wav")
    check(wav if (len(sys.argv) > 1 and sys.argv[1] == "check") else build_audio())
