"""series_sfx.py -- the musical signature shared by every episode of the series.

    music_hit() -> mono float array at `sr`, peak 0.9

Three plucked veena/sitar notes (D3-A3-D4, an octave up) with a gentle meend into
pitch and a 1.5 s decay, plus one low tabla "dhin".  Synthesised, no samples.
"""

import numpy as np

SR = 48000
D3, A3, D4 = 146.83, 220.00, 293.66


def _t(dur, sr):
    return np.arange(int(round(dur * sr))) / sr


def _pluck(freq, dur, sr=SR, bend=0.009, seed=1):
    """Additive plucked string: starts a little flat and bends up into the note,
    upper harmonics dying faster than the fundamental."""
    t = _t(dur, sr)
    f = freq * (1 - bend * np.exp(-t / 0.12))
    ph = 2 * np.pi * np.cumsum(f) / sr
    y = np.zeros_like(t)
    for k, a, tau in ((1, 1.00, 0.55), (2, 0.45, 0.30), (3, 0.26, 0.18),
                      (4, 0.13, 0.10), (5, 0.07, 0.06)):
        y += a * np.sin(k * ph + 0.3 * k) * np.exp(-t / tau)
    pick = np.random.default_rng(seed).standard_normal(len(t))
    y += 0.08 * pick * np.exp(-t / 0.004)
    return y * (1 - np.exp(-t / 0.002))


def _tabla_dhin(dur=0.9, sr=SR):
    """Low membrane thump: pitch drops as the skin relaxes, with the slap on top."""
    t = _t(dur, sr)
    f = 72 + 58 * np.exp(-t / 0.05)
    ph = 2 * np.pi * np.cumsum(f) / sr
    body = np.sin(ph) * np.exp(-t / 0.22)
    ring = 0.35 * np.sin(1.58 * ph) * np.exp(-t / 0.12)
    slap = np.random.default_rng(5).standard_normal(len(t))
    slap = np.convolve(slap, np.ones(48) / 48, mode="same")
    slap = slap * np.exp(-t / 0.015) * 0.5
    return (body + ring + slap) * (1 - np.exp(-t / 0.001))


def music_hit(sr=SR, dur=2.2):
    """The series sting: D3-A3-D4 plucked with a bend, over a low tabla dhin."""
    out = np.zeros(int(round(dur * sr)))
    for f, off, g, seed in ((D3, 0.000, 1.00, 1),
                            (A3, 0.028, 0.90, 2),
                            (D4, 0.056, 0.80, 3)):
        p = _pluck(f, dur - off, sr, seed=seed)
        i = int(round(off * sr))
        n = min(len(p), len(out) - i)
        out[i:i + n] += g * p[:n]
    d = _tabla_dhin(0.9, sr)
    n = min(len(d), len(out))
    out[:n] += 0.85 * d[:n]
    return out / np.abs(out).max() * 0.9


if __name__ == "__main__":
    import wave

    x = music_hit()
    with wave.open("series_sfx_preview.wav", "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((x * 32767).astype("<i2").tobytes())
    print("wrote series_sfx_preview.wav, %d samples" % len(x))
