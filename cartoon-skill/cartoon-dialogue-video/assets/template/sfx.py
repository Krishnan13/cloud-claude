"""
sfx -- a small sound palette for narrated scenes, synthesised in code.

Each sound means one thing, in every scene:

    swish      a figure is drawn
    settle     a piece lands in place
    tick(n)    the n-th thing is counted (pitch rises with n)
    low        something is missing
    chime      a result is revealed -- only once the evidence is on screen
    chord      the rule is established

No downloads and no licences: the wavs are generated once into sfx/ next to this
file. Levels sit 8-12 dB under the narration's speaking level -- noticed, never competing.

    SFX=0 manim ...   renders without any of them (for A/B listening).

Final renders: use --disable_caching. Reused cached clips shifted the whole
soundtrack by up to ~80 ms in testing; fresh renders are exact.
"""

import os
import wave
from pathlib import Path

import numpy as np

SR = 24000  # same rate as the narration audio
DIR = Path(__file__).resolve().parent / "sfx"
ENABLED = os.environ.get("SFX", "1") != "0"

# G major pentatonic from G4: counting always climbs, never lands on a sour note.
PENTATONIC = [0, 2, 4, 7, 9, 12, 14, 16, 19, 21, 24]


def _t(dur):
    return np.arange(int(SR * dur)) / SR


def _env(t, attack, tau):
    return (1 - np.exp(-t / attack)) * np.exp(-t / tau)


def _pluck(freq):
    # Marimba-like: warm fundamental plus a quick, quiet fourth harmonic.
    t = _t(0.4)
    return _env(t, 0.002, 0.07) * (np.sin(2 * np.pi * freq * t)
                                   + 0.25 * np.exp(-t / 0.02) * np.sin(2 * np.pi * 4 * freq * t))


def _swish():
    # Band-limited noise with a quick rise and a long tail: a soft pencil stroke.
    n = int(SR * 0.7)
    spectrum = np.fft.rfft(np.random.default_rng(7).standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR)
    band = np.exp(-0.5 * (np.log(np.maximum(f, 1) / 2500) / 0.6) ** 2)
    noise = np.fft.irfft(spectrum * band, n)
    t = _t(0.7)
    return noise * np.sin(np.pi * np.minimum(t / 0.2, 1) / 2) * np.exp(-np.maximum(t - 0.2, 0) / 0.15)


def _settle():
    # A soft wooden "thock": pitch drops as it lands.
    t = _t(0.18)
    freq = 110 + 80 * np.exp(-t / 0.03)
    return _env(t, 0.001, 0.035) * np.sin(2 * np.pi * np.cumsum(freq) / SR)


def _low():
    # A muted, open low tone -- "something is missing", never "wrong".
    t = _t(1.1)
    return _env(t, 0.06, 0.35) * (np.sin(2 * np.pi * 196 * t) + 0.3 * np.sin(2 * np.pi * 392 * t))


def _strum(freqs, gap, attack, tau, dur):
    t = _t(dur)
    out = np.zeros_like(t)
    for i, f in enumerate(freqs):
        s = int(i * gap * SR)
        tt = t[: len(t) - s]
        out[s:] += _env(tt, attack, tau) * (np.sin(2 * np.pi * f * tt)
                                            + 0.2 * np.exp(-tt / 0.2) * np.sin(2 * np.pi * 2 * f * tt))
    return out


def _chime():
    # G major triad, quickly strummed: a discovery.
    return _strum([392.0, 493.9, 587.3], 0.035, 0.004, 0.45, 1.5)


def _chord():
    # A fuller, slower G major chord: closure.
    return _strum([196.0, 293.7, 392.0, 493.9], 0.02, 0.04, 0.9, 2.6)


def _file(name):
    path = DIR / f"{name}.wav"
    if not path.exists():
        if name.startswith("tick"):
            x = _pluck(392.0 * 2 ** (PENTATONIC[int(name[4:]) - 1] / 12))
        else:
            x = {"swish": _swish, "settle": _settle, "low": _low,
                 "chime": _chime, "chord": _chord}[name]()
        x = x / np.abs(x).max() * 0.89  # peak -1 dBFS; add_sound's gain sets the level
        DIR.mkdir(exist_ok=True)
        with wave.open(str(path), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes((x * 32767).astype(np.int16).tobytes())
    return path


def _play(scene, name, gain, offset):
    if ENABLED:
        scene.add_sound(str(_file(name)), time_offset=offset, gain=gain)


def swish(scene, offset=0.0):
    _play(scene, "swish", -15, offset)


def settle(scene, offset=0.0):
    _play(scene, "settle", -16, offset)


def tick(scene, n, offset=0.0):
    _play(scene, f"tick{n}", -15, offset)


def low(scene, offset=0.0):
    _play(scene, "low", -20, offset)


def chime(scene, offset=0.0):
    _play(scene, "chime", -13, offset)


def chord(scene, offset=0.0):
    _play(scene, "chord", -13, offset)


def lagged_starts(n, lag_ratio, run_time):
    """Start times of each item in LaggedStart(..., lag_ratio, run_time=run_time)."""
    each = run_time / (1 + lag_ratio * (n - 1))
    return [i * lag_ratio * each for i in range(n)]
