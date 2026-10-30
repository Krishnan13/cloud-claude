"""sound_scene2.py -- builds build/scene2_audio.wav for the 38.0 s scene 2 ink cut.

    python sound_scene2.py            # beds + voices -> amix -> master, then the checks
    python sound_scene2.py check      # re-print the level windows only

Ambience and effects are synthesised with numpy and the helpers imported from
sound_scene1.py; the narration comes from audio/, the "tick" from the shared sfx
palette and the series sting from series_sfx.py.
"""

import json
import os
import re
import subprocess
import sys

import numpy as np

import sfx
import series_sfx
import sound_scene1 as s1

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
SR = s1.SR
DUR = 38.0
N = int(round(DUR * SR))

VOICES = [
    ("n1_neighbour.mp3", 13.6),
    ("o_suresh.mp3", 15.9),
    ("o_ramesh.mp3", 16.05),
    ("sting_yabuu.mp3", 33.3),
]

_t = s1._t
_norm = s1._norm
_rms_norm = s1._rms_norm
_fft_filter = s1.fft_filter
_vramp = s1.vramp
_pink = s1._pink


# ------------------------------------------------------------------ generators
def _formants(x, centers, widths):
    """Sum of gaussian bands around the given formant centres (one FFT)."""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    g = np.zeros_like(f)
    for c, w in zip(centers, widths):
        g += np.exp(-0.5 * ((f - c) / w) ** 2)
    return np.fft.irfft(X * g, len(x))


def _chirp(rng, dur):
    t = _t(dur)
    f0 = rng.uniform(2600, 5200)
    f1 = f0 * rng.uniform(0.60, 1.45)
    f = f0 + (f1 - f0) * t / dur
    y = np.sin(2 * np.pi * np.cumsum(f) / SR + 0.4 * np.sin(2 * np.pi * 90 * t))
    return y * np.sin(np.pi * t / dur) ** 1.6


def _bird_call(rng):
    parts = []
    for _ in range(int(rng.integers(1, 4))):
        parts.append(_chirp(rng, rng.uniform(0.035, 0.075)))
        parts.append(np.zeros(int(rng.uniform(0.02, 0.06) * SR)))
    return _norm(np.concatenate(parts), 1.0)


def birds(bus, t0, t1, rate, gain, seed, pan=0.0, spread=0.7):
    """Sparse overlapping chirps between t0 and t1."""
    rng = np.random.default_rng(seed)
    tcur = t0 + rng.uniform(0, 1 / rate)
    while tcur < t1:
        bus.add(_bird_call(rng), tcur, gain=gain * rng.uniform(0.6, 1.1),
                pan=float(np.clip(pan + rng.uniform(-spread, spread), -1, 1)))
        tcur += rng.exponential(1 / rate)


def rooster():
    """Rising-falling "ku-ka-doo" from three glides with a rough buzz."""
    def glide(f0, f1, dur, peak, amp):
        t = _t(dur)
        u = t / dur
        f = f0 + (f1 - f0) * u + (peak - (f0 + f1) / 2) * np.sin(np.pi * u)
        f += 12 * np.sin(2 * np.pi * 26 * t)
        ph = 2 * np.pi * np.cumsum(f) / SR
        y = sum(a * np.sin(k * ph) for k, a in ((1, 1.0), (2, 0.40),
                                                (3, 0.20), (4, 0.10)))
        y *= np.minimum(t / 0.02, 1) * np.minimum((dur - t) / 0.03, 1)
        return _norm(y, 1.0) * amp

    out = np.zeros(int(0.95 * SR))
    for i, (f0, f1, dur, peak, amp) in enumerate(
            ((600, 450, 0.17, 560, 0.8), (820, 620, 0.13, 800, 1.0),
             (680, 470, 0.48, 1020, 0.9))):
        a = glide(f0, f1, dur, peak, amp)
        s = int(i * 0.18 * SR)
        out[s:s + len(a)] += a
    return _norm(out, 0.85)


def breeze(dur=7.0, seed=11):
    t = _t(dur)
    x = _rms_norm(_fft_filter(_pink(len(t), seed), lo=80, hi=700), 1.0)
    swell = 0.55 + 0.45 * np.sin(2 * np.pi * 0.17 * t + 1.1) ** 2
    env = np.minimum(t / 1.2, 1) * np.minimum((dur - t) / 1.5, 1)
    return x * swell * env


def walk(bus, t0, t1, gain, seed, pan_a=-0.25, pan_b=0.25, rate=2.5):
    """Two people on dirt: overlapping steps, slightly offset."""
    rng = np.random.default_rng(seed)
    tcur = t0
    k = 0
    while tcur < t1:
        bus.add(s1.footstep(seed + k % 5), tcur,
                gain=gain * rng.uniform(0.75, 1.0), pan=pan_a)
        if tcur + 0.11 < t1:
            bus.add(s1.footstep(seed + k % 5 + 11), tcur + 0.11,
                    gain=gain * rng.uniform(0.7, 0.95), pan=pan_b)
        tcur += 1 / rate + rng.uniform(-0.02, 0.02)
        k += 1


def murmur_voice(dur, rng, f0):
    """Wordless voice: glottal buzz through moving formants, gated into syllables."""
    t = _t(dur)
    vib = 1 + 0.02 * np.sin(2 * np.pi * rng.uniform(4, 6) * t)
    ph = 2 * np.pi * np.cumsum(f0 * vib) / SR
    buzz = 2 * ((ph / (2 * np.pi)) % 1.0) - 1
    buzz = _formants(buzz, [rng.uniform(400, 700), rng.uniform(1100, 1900),
                            rng.uniform(2400, 3000)], [90, 180, 280])

    env = np.zeros_like(t)
    cur = rng.uniform(0, 0.2)
    while cur < dur:
        d = rng.uniform(0.09, 0.28)
        i = int(cur * SR)
        j = min(int((cur + d) * SR), len(t))
        if j > i:
            env[i:j] = np.sin(np.pi * np.arange(j - i) / (j - i)) ** 1.2
        cur += d + rng.uniform(0.05, 0.20)

    whisper = _formants(rng.standard_normal(len(t)), [1500, 2500], [600, 800])
    return (0.8 * buzz + 0.6 * whisper) * env


def murmur_bed(bus, t0, t1, gain, seed, count=14):
    rng = np.random.default_rng(seed)
    span = t1 - t0
    for _ in range(count):
        dur = span * rng.uniform(0.5, 1.0)
        v = murmur_voice(dur, rng, rng.uniform(88, 150))
        bus.add(v, t0 + rng.uniform(0, span - dur),
                gain=gain * rng.uniform(0.7, 1.2), pan=rng.uniform(-0.8, 0.8))


def room_tone(dur=8.7, seed=41):
    t = _t(dur)
    x = _rms_norm(_fft_filter(_pink(len(t), seed), lo=40, hi=400), 1.0)
    drift = 0.8 + 0.2 * np.sin(2 * np.pi * 0.11 * t)
    env = np.minimum(t / 0.5, 1) * np.minimum((dur - t) / 0.8, 1)
    return x * drift * env


def wood_creak(dur=0.7, seed=17):
    t = _t(dur)
    u = t / dur
    body = _fft_filter(np.random.default_rng(seed).standard_normal(len(t)),
                       lo=350, hi=1500)
    grain = 0.4 + 0.6 * (0.5 + 0.5 * np.sin(2 * np.pi * (28 + 22 * u) * t))
    env = np.sin(np.pi * u) ** 0.6
    return _norm(body * grain * env, 0.7)


def cloth_pat(dur=0.14, seed=19):
    t = _t(dur)
    x = _fft_filter(np.random.default_rng(seed).standard_normal(len(t)),
                    lo=120, hi=1400)
    env = (1 - np.exp(-t / 0.004)) * np.exp(-t / 0.035)
    return _norm(x * env, 0.6)


def puppy_yip(dur=0.15, seed=23):
    t = _t(dur)
    u = t / dur
    f = 750 + 950 * np.sin(np.pi * u ** 0.7)
    ph = 2 * np.pi * np.cumsum(f) / SR
    y = np.sin(ph) + 0.40 * np.sin(2 * ph) + 0.20 * np.sin(3 * ph)
    y += 0.30 * _fft_filter(np.random.default_rng(seed).standard_normal(len(t)),
                            lo=800, hi=4000) * np.exp(-t / 0.02)
    env = np.minimum(t / 0.006, 1) * np.minimum((dur - t) / 0.02, 1) ** 1.2
    return _norm(y * env, 0.8)


def tinkle(dur, seed=27):
    rng = np.random.default_rng(seed)
    out = np.zeros(int(dur * SR))
    tcur = 0.02
    while tcur < dur - 0.02:
        f0 = rng.uniform(2600, 5200)
        t = _t(rng.uniform(0.10, 0.30))
        y = (np.sin(2 * np.pi * f0 * t) + 0.5 * np.sin(2 * np.pi * 1.5 * f0 * t)
             + 0.3 * np.sin(2 * np.pi * 2.3 * f0 * t))
        y *= (1 - np.exp(-t / 0.001)) * np.exp(-t / 0.05)
        i = int(tcur * SR)
        n = min(len(y), len(out) - i)
        out[i:i + n] += y[:n] * rng.uniform(0.5, 1.0)
        tcur += rng.uniform(0.03, 0.11)
    return _norm(out, 0.6)


def kiss(dur=0.30, seed=29):
    t = _t(dur)
    u = t / dur
    rng = np.random.default_rng(seed)
    body = np.sin(2 * np.pi * np.cumsum(220 + 500 * np.exp(-t / 0.05)) / SR)
    body *= np.exp(-t / 0.06)
    pop = _fft_filter(rng.standard_normal(len(t)), lo=200, hi=2500)
    pop *= np.exp(-t / 0.03)
    smack = _fft_filter(rng.standard_normal(len(t)), lo=800, hi=5000)
    smack *= np.exp(-np.maximum(t - 0.08, 0) / 0.02) * (u > 0.3)
    return _norm(0.6 * body + 0.7 * pop + 0.4 * smack, 0.7)


# ------------------------------------------------------------------ beds
def build_beds():
    os.makedirs(BUILD, exist_ok=True)
    bus = s1.Bus()

    # 0.0-7.0 morning lane: birds, rooster, two people on dirt, faint breeze
    birds(bus, 0.0, 7.0, rate=2.2, gain=0.016, seed=101, pan=-0.1, spread=0.8)
    bus.add(rooster(), 0.6, gain=0.045, pan=0.1)
    # side walk: they stop to search (3.25-4.3) and freeze at the crowd (5.6-6.3), then hurry
    walk(bus, 0.4, 3.25, gain=0.050, seed=200)
    walk(bus, 4.3, 5.6, gain=0.050, seed=201)
    walk(bus, 6.3, 7.0, gain=0.055, seed=202)
    bus.add(breeze(), 0.0, gain=0.0045, pan=-0.2)

    # 7.0-19.0 at the gate: murmur bed (dips under the neighbour line, then
    # fades to silence by 20.8), birds lower
    murmur = s1.Bus()
    murmur_bed(murmur, 7.0, 20.8, gain=0.0060, seed=301)
    tm = np.arange(len(murmur.x)) / SR
    env = ((1 - _vramp(tm, 19.0, 20.8))
           * (1 - 0.6 * (_vramp(tm, 13.55, 13.75) - _vramp(tm, 15.2, 15.45))))
    murmur.x *= env[:, None]
    bus.x += murmur.x

    birds(bus, 7.0, 19.0, rate=0.9, gain=0.009, seed=102, pan=0.0, spread=0.9)
    walk(bus, 7.2, 9.1, gain=0.045, seed=210)
    bus.add(cloth_pat(seed=19), 11.85, gain=0.030, pan=-0.1)
    bus.add(cloth_pat(seed=20), 12.00, gain=0.030, pan=0.1)

    # 19.0-24.0 at the window: murmur gone, faint room tone, hands on the bars
    bus.add(room_tone(), 20.8, gain=0.0030)
    bus.add(wood_creak(), 20.9, gain=0.030, pan=0.15)

    # 24.0-29.5 the reveal: yips, collar jingle, two kisses
    for t0 in (24.4, 26.1, 28.4):
        bus.add(puppy_yip(), t0, gain=0.050, pan=0.0)
    bus.add(tinkle(5.0), 24.2, gain=0.012, pan=0.25)
    bus.add(kiss(), 25.3, gain=0.045, pan=0.0)
    bus.add(kiss(seed=30), 26.9, gain=0.045, pan=0.0)

    # 29.5-33.2 the faces: faint birds far away, a tick as the heads turn
    birds(bus, 29.5, 33.2, rate=0.35, gain=0.006, seed=103, pan=0.0, spread=1.0)
    tick, sr = s1.read_wav(str(sfx._file("tick1")))
    bus.add(s1.resample(tick, sr), 31.0, gain=0.030, pan=0.0)

    # 33.2 freeze: short soft whoosh
    bus.add(s1.whoosh(0.3, seed=6), 35.7, gain=0.060, pan=0.0)

    # mastering squeezes the voice peaks to reach -14 LUFS; drop the ambience so
    # it stays ~20 dB under the voices in the finished mix.  The series hit below
    # is added after this, at full level.
    bus.x *= 10 ** (-5.0 / 20)

    # 36.0 the series sting
    bus.add(series_sfx.music_hit(), 35.85, gain=0.280, pan=0.0)

    x = bus.x[:N].copy()
    peak = np.abs(x).max()
    if peak > 0.98:
        x *= 0.98 / peak

    out = os.path.join(BUILD, "scene2_beds.wav")
    s1.write_wav(out, x)
    print("beds:", out, "rms %.1f dB" % (20 * np.log10(max(s1._rms(x), 1e-9))))
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
        chains.append(
            f"[{i}:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=mono,"
            f"pan=stereo|c0={gl:.4f}*c0|c1={gr:.4f}*c0,"
            f"alimiter=limit=0.36:attack=2:release=80:level=false:latency=true,"
            f"adelay={ms}|{ms}[a{i}]")
    mix = ("".join(f"[a{i}]" for i in range(len(inputs)))
           + f"amix=inputs={len(inputs)}:normalize=0:duration=longest,"
             f"apad=whole_dur={DUR},atrim=0:{DUR},"
             f"afade=t=out:st=37.2:d=0.8")
    graph = ";".join(chains) + ";" + mix
    cmd_in = sum([["-i", p] for p in inputs], [])
    ln = "loudnorm=I=-14:TP=-1.5:LRA=25"

    # pass 1: measure, so pass 2 can normalise linearly without moving the length
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *cmd_in,
                        "-filter_complex", graph + f",{ln}:print_format=json[o]",
                        "-map", "[o]", "-f", "null", "-"],
                       capture_output=True, text=True, check=True)
    m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr, re.S).group(0))
    # With this much near-silence the programme is peakier than scene 1's, so a
    # linear +11 dB lift overshoots TP and loudnorm would fall back to dynamic
    # mode -- boosting the quiet ambience by ~25 dB.  Apply the loudnorm linear
    # gain explicitly and enforce TP with a limiter instead, which keeps the beds
    # well under the voices.
    gain = -14.0 - float(m["input_i"])
    # a fast peak limiter (rather than a slow one) keeps the loudness that the
    # linear gain adds; the ceiling leaves room for inter-sample peaks (the
    # 16-bit true peak measures ~0.8 dB above it)
    tp = 10 ** (-2.3 / 20)
    limit = (f"alimiter=limit={tp:.4f}:attack=0.5:release=30:"
             f"level=false:latency=true")

    def master_i(g):
        """Loudness after the linear gain and the TP limiter."""
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *cmd_in,
                            "-filter_complex",
                            graph + f",volume={g:.3f}dB,{limit},"
                                    f"{ln}:print_format=json[o]",
                            "-map", "[o]", "-f", "null", "-"],
                           capture_output=True, text=True, check=True)
        return float(json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}",
                                          r.stderr, re.S).group(0))["input_i"])

    # limiting costs a little loudness: converge the gain onto -14 LUFS, but do
    # not push further once the limiter has flattened the level (it would only
    # squeeze the voices harder)
    for _ in range(8):
        i = master_i(gain)
        if abs(i + 14.0) < 0.1:
            break
        gain = min(max(gain + 0.6 * (-14.0 - i), 7.0), 16.5)

    out = os.path.join(BUILD, "scene2_audio.wav")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *cmd_in,
                    "-filter_complex",
                    graph + (f",volume={gain:.3f}dB,{limit},"
                             f"aresample=48000,atrim=0:{DUR}[o]"),
                    "-map", "[o]", "-ar", "48000", "-ac", "2",
                    "-c:a", "pcm_s16le", out], check=True)
    print("audio:", out, "master %.1f LUFS (gain %+.1f dB)" % (master_i(gain), gain))
    return out


# ------------------------------------------------------------------ checks
def check(path):
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", path],
                       capture_output=True, text=True, check=True).stdout.strip()
    print("duration: %s s" % d)
    for a, b in ((0, 7), (13.6, 15.3), (15.9, 17.5), (24, 29.5), (33.4, 36)):
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-ss", str(a),
                            "-to", str(b), "-i", path, "-af", "volumedetect",
                            "-f", "null", "-"], capture_output=True, text=True)
        mv = re.search(r"mean_volume:\s*(-?[\d.]+) dB", r.stderr)
        pv = re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr)
        print(f"  {a:>5}-{b:<4}s  mean {mv.group(1) if mv else '?':>6} dB"
              f"  max {pv.group(1) if pv else '?':>6} dB")


if __name__ == "__main__":
    wav = os.path.join(BUILD, "scene2_audio.wav")
    check(wav if (len(sys.argv) > 1 and sys.argv[1] == "check") else build_audio())
