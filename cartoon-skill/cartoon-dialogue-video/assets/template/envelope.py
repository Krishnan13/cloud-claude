"""envelope.py -- loudness envelope of a voice clip, one value per video frame.

env = voice_envelope("audio/x.mp3")      # numpy array, values 0..1, 30 per second
open_amt = mouth_at(env, t_local)        # t_local = seconds since the clip started
"""
import subprocess
import numpy as np

SR = 44100


def decode_mono(path, sr=SR):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr),
           "-f", "s16le", "-"]
    raw = subprocess.run(cmd, check=True, stdout=subprocess.PIPE).stdout
    return np.frombuffer(raw, dtype="<i2").astype(np.float64) / 32768.0, sr


def voice_envelope(path, fps=30, gate=0.07, attack=0.65, release=0.30):
    x, sr = decode_mono(path)
    n = int(np.ceil(len(x) / sr * fps))
    half = int(sr / fps)                     # window = 2/fps, centred on the frame time
    rms = np.zeros(n)
    for i in range(n):
        c = int(round(i / fps * sr))
        seg = x[max(0, c - half): c + half]
        rms[i] = np.sqrt(np.mean(seg ** 2)) if len(seg) else 0.0
    active = rms[rms > 0.05 * rms.max()]
    p95 = np.percentile(active, 95) if len(active) else 1.0
    e = np.clip(rms / max(p95, 1e-9), 0, 1.0)
    out = np.zeros(n)                        # attack / release smoothing
    prev = 0.0
    for i, v in enumerate(e):
        k = attack if v > prev else release
        prev = prev + k * (v - prev)
        out[i] = prev
    out = np.clip((out - gate) / (1 - gate), 0, 1)   # near-silence -> fully closed
    return out


def mouth_at(env, t_local, fps=30):
    """Envelope value (0..1) at t_local seconds into the clip; 0 outside the clip."""
    f = t_local * fps
    if f < 0 or f > len(env) - 1:
        return 0.0
    return float(np.interp(f, np.arange(len(env)), env))
