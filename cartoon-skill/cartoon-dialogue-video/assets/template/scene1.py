"""Scene 1 — night bus (ink style). 45.5 s.

    manim -qm --frame_rate 24 --disable_caching scene1.py Scene1
Shot list and acting live in this file; every pose is a function of the master
clock T. Characters update on twos (12 poses/s); the world moves every frame.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
from manim import *

from ink import person, RAMESH, SURESH, INK, blob, curve, _p
from envelope import voice_envelope, mouth_at
from style_test import window_layer, light_sweep, HERE

DUR = 45.5
# voice start times (must match sound_scene1.py)
LINES = {"s1": ("s1_suresh.mp3", 8.8), "r1": ("r1_ramesh.mp3", 13.8), "s2": ("s2_suresh.mp3", 24.8),
         "r2": ("r2_ramesh.mp3", 29.2), "s3": ("s3_suresh.mp3", 33.8)}
ENV = {k: (voice_envelope(str(HERE / "audio" / f)), t0) for k, (f, t0) in LINES.items()}


def talk(who, t):
    keys = [k for k in ENV if k[0] == who]
    return max(mouth_at(ENV[k][0], t - ENV[k][1]) for k in keys)


def ease(x):
    x = np.clip(x, 0, 1)
    return x * x * (3 - 2 * x)


def key(t, keys):
    if t <= keys[0][0]:
        return keys[0][1]
    for (a, va), (b, vb) in zip(keys, keys[1:]):
        if t <= b:
            k = ease((t - a) / (b - a))
            if isinstance(va, tuple):
                return tuple(np.add(np.multiply(va, 1 - k), np.multiply(vb, k)))
            return va + (vb - va) * k
    return keys[-1][1]


def blink(t, times):
    return 0.0 if any(0 <= t - b < 0.11 for b in times) else 1.0


# ------------------------------------------------------------------ bus motion
def speed(t):
    return key(t, [(0, 1.0), (3.9, 1.0), (4.3, 0.0), (7.6, 0.0), (8.4, 1.0), (37.6, 1.0), (38.4, 0.0)])


_G = np.arange(0, DUR + 0.5, 1 / 240)
_D = np.concatenate([[0], np.cumsum([speed(x) for x in _G[1:]]) / 240])


def dist(t):
    return float(np.interp(t, _G, _D))


def shake(t):
    s = speed(t)
    y = s * (0.018 * np.sin(2 * np.pi * 5.3 * t) + 0.012 * np.sin(2 * np.pi * 2.1 * t + 1))
    for at, amp in ((11.0, 0.09),):                     # pothole
        b = t - at
        if 0 <= b < 0.5:
            y += -amp * np.sin(np.pi * b / 0.5) * np.exp(-3 * b)
    return y


# ------------------------------------------------------------------ camera
TWO = ((0.0, 0.0), 1.0, (0.0, 0.0))                     # (focus, zoom, where focus lands on screen)
RAM_MCU = ((-2.35, 0.45), 1.65, (-1.5, 0.05))
SUR_CU = ((2.5, 0.85), 1.9, (1.7, -0.55))

SHOTS = [  # (start, kind, camera)
    (0.0, "street", None),
    (3.5, "bus", TWO),
    (13.6, "bus", RAM_MCU),
    (19.0, "bus", TWO),
    (21.1, "bus", SUR_CU),
    (29.0, "bus", RAM_MCU),
    (33.6, "bus", TWO),
    (39.8, "stop", None),
]


def shot_at(t):
    cur = SHOTS[0]
    for s in SHOTS:
        if t >= s[0]:
            cur = s
    return cur


def apply_cam(g, cam, t):
    (fx, fy), z, (sx, sy) = cam
    if cam is SUR_CU:                                   # snap zoom on "ಐದು ಲಕ್ಷ"
        z *= key(t, [(22.2, 1.0), (22.34, 1.18), (24.6, 1.18), (24.61, 1.0)])
    if cam is TWO and t < 13.6:                         # gentle push during boarding / S1
        z *= key(t, [(3.5, 1.0), (13.6, 1.06)])
    g.scale(z, about_point=_p(fx, fy)).shift(_p(sx - fx, sy - fy))
    return g


# ------------------------------------------------------------------ acting
def ramesh_pose(tc):
    m = talk("r", tc)
    P = dict(mouth=m, eye_open=blink(tc, [5.2, 10.4, 16.9, 23.0, 27.6, 31.8, 36.1]), smile=0.2)
    # looking out of the window until Suresh calls him
    P["yaw"] = key(tc, [(0, -0.7), (9.25, -0.7), (9.6, 0.8),            # turns at "ರಮೇಶಾ"
                        (14.4, 0.8), (14.6, -0.35), (15.0, -0.35), (15.2, 0.3), (15.5, 0.3), (15.7, 0.85),  # secret glance
                        (37.5, 0.85), (37.75, -0.6), (38.1, -0.6), (38.3, 0.5)])
    P["look"] = key(tc, [(0, (-0.9, 0.15)), (9.25, (-0.9, 0.15)), (9.6, (0.9, 0.05)),
                         (14.4, (0.9, 0.05)), (14.6, (-0.9, 0.0)), (15.2, (0.9, 0.0)), (15.7, (0.9, 0.05)),
                         (37.5, (0.9, 0.05)), (37.75, (-0.9, 0.1)), (38.3, (0.9, 0.0))])
    P["brow"] = key(tc, [(0, 0.0), (9.4, 0.0), (9.6, 0.7), (10.2, 0.25), (13.8, 0.25), (14.1, 0.6), (16.0, 0.3),
                         (29.2, 0.3), (29.5, 0.55), (33.4, 0.3), (37.6, 0.3), (37.8, 0.9), (38.6, 0.3)])
    P["smile"] = key(tc, [(0, 0.15), (9.6, 0.15), (10.0, 0.85), (13.6, 0.6), (19.0, 0.2), (21.0, 0.45), (29.2, 0.8)])
    P["lean"] = key(tc, [(0, 0.0), (13.4, 0.0), (13.9, 0.35), (21.0, 0.35), (21.5, 0.1), (29.0, 0.1), (29.3, 0.3), (33.5, 0.1)])
    P["tilt"] = key(tc, [(0, 0.0), (13.4, 0.0), (13.9, 0.4), (19.0, 0.4), (19.5, 0.1)])
    # nods: firm "yes" on R2
    nod = sum(0.12 * np.exp(-((tc - c) / 0.12) ** 2) for c in (29.6, 30.5, 32.2))
    P["bob"] = -nod
    # hand gesture while telling the news, and the "plan" palm on R2
    P["hand_r"] = key(tc, [(0, (0.5, -2.05)), (15.6, (0.5, -2.05)), (16.0, (1.35, -1.05)), (18.4, (1.35, -1.05)),
                           (18.8, (0.5, -2.05)), (29.9, (0.5, -2.05)), (30.3, (1.3, -0.85)), (32.8, (1.3, -0.85)), (33.2, (0.5, -2.05))])
    P["hand_r_open"] = key(tc, [(0, 0.2), (15.6, 0.2), (16.0, 1.0), (18.4, 1.0), (18.8, 0.2), (29.9, 0.2), (30.3, 1.0),
                                (32.8, 1.0), (33.2, 0.2)])
    P["hand_r_curl"] = key(tc, [(0, 0.5), (15.6, 0.5), (16.0, 0.0), (18.4, 0.0), (18.8, 0.5), (29.9, 0.5), (30.3, 0.0),
                                (32.8, 0.0), (33.2, 0.5)])
    P["hand_r_dir"] = key(tc, [(0, -1.2), (15.6, -1.2), (16.0, 1.25), (18.4, 1.25), (18.8, -1.2), (29.9, -1.2), (30.3, 1.3),
                               (32.8, 1.3), (33.2, -1.2)])
    # his stop: stands up and squeezes out past Suresh
    up = key(tc, [(37.9, 0.0), (38.4, 1.0)])
    P["standing"] = up > 0.5
    if up > 0.5:
        P.update(bag_at="hand_r", hand_r=(1.35, -2.3), hand_l=(-1.4, -2.3), yaw=0.5, lean=0.0, tilt=0.0)
    x = key(tc, [(38.4, -2.65), (39.6, 7.8)])
    y = -0.6 + 1.15 * up + (0.05 * abs(np.sin(tc * 9)) if tc > 38.4 else 0)
    return P, x, y


def suresh_pose(tc):
    m = talk("s", tc)
    P = dict(mouth=m, eye_open=blink(tc, [6.1, 12.0, 17.6, 26.4, 31.0, 35.5]))
    # boarding: walks in standing (5.0-5.7), spots Ramesh, waves (unnoticed!), sits (6.8-7.4)
    sit = key(tc, [(6.8, 0.0), (7.35, 1.0)])
    standing = sit < 0.6
    P["standing"] = standing
    x = key(tc, [(4.7, 7.6), (5.7, 3.3), (6.8, 3.3), (7.35, 2.55)])
    walking = 4.7 < tc < 5.7
    y = key(tc, [(6.8, 0.6), (7.25, -0.62), (7.4, -0.5), (7.5, -0.55)]) + (0.07 * abs(np.sin(tc * 10)) if walking else 0)
    P["stride"] = np.sin(tc * 10) if walking else 0.0
    P["yaw"] = key(tc, [(0, -0.5), (5.6, -0.5), (5.8, -0.85), (6.9, -0.85), (7.4, -0.3), (8.4, -0.3), (8.7, -0.85),
                        (37.5, -0.85), (37.8, -0.6), (38.8, 0.4), (39.6, 0.6)])
    P["look"] = key(tc, [(0, (-0.6, 0.0)), (5.8, (-0.9, 0.0)), (38.6, (-0.9, 0.0)), (39.0, (0.9, 0.0))])
    P["brow"] = key(tc, [(0, 0.2), (5.7, 0.2), (5.85, 0.9), (6.6, 0.5), (8.6, 0.5), (8.8, 0.6), (12.5, 0.6), (13.8, 0.3),
                         (21.5, 0.3), (22.2, 1.0), (24.4, 0.9), (24.8, 0.9), (28.6, 0.7), (33.6, 0.4), (34.0, 0.5), (37.4, 0.5)])
    P["worry"] = key(tc, [(0, 0.0), (19.0, 0.0), (19.3, 0.8), (21.0, 0.8), (21.6, 0.0)])
    P["wide"] = key(tc, [(0, 0.0), (22.15, 0.0), (22.3, 1.0), (24.6, 1.0), (24.8, 0.6), (28.6, 0.4), (29.5, 0.0)])
    P["smile"] = key(tc, [(0, 0.3), (5.8, 0.9), (8.6, 0.6), (13.8, 0.4), (19.0, -0.2), (21.0, -0.2), (22.0, 0.1),
                          (24.8, 0.9), (29.0, 0.7), (34.0, 0.8)])
    P["mouth"] = max(m, key(tc, [(22.15, 0.0), (22.3, 0.45), (24.4, 0.45), (24.7, 0.0)]))   # jaw drop at "ಐದು ಲಕ್ಷ"
    P["lean"] = key(tc, [(0, 0.0), (8.6, 0.0), (9.0, -0.15), (13.6, -0.1), (38.4, -0.1), (38.7, 0.3), (39.6, 0.1)])
    P["tilt"] = key(tc, [(0, 0.0), (11.3, 0.0), (11.7, -0.5), (13.3, -0.5), (13.8, 0.0), (24.8, 0.0), (25.2, -0.3), (28.6, -0.3), (29.0, 0.0)])
    P["bob"] = 0.1 * np.exp(-((tc - 22.3) / 0.12) ** 2) - sum(0.1 * np.exp(-((tc - c) / 0.12) ** 2) for c in (34.6, 35.5))
    # hands: wave while boarding, open palm on "ಎಂತ ಮತ್ತೆ ವಿಶೇಷ", palm toward Ramesh on S3, bye-wave
    wave = 0.18 * np.sin(tc * 14)
    P["hand_l"] = key(tc, [(0, (-1.45, -2.3)), (5.8, (-1.45, -2.3)), (6.0, (-1.6 + wave, 0.25)), (6.6, (-1.6 + wave, 0.25)),
                           (6.8, (-0.5, -2.05)), (11.3, (-0.5, -2.05)), (11.7, (-1.75, -1.0)), (13.3, (-1.75, -1.0)), (13.7, (-0.5, -2.05)),
                           (34.4, (-0.5, -2.05)), (34.8, (-1.7, -1.05)), (37.0, (-1.7, -1.05)), (37.4, (-0.5, -2.05)),
                           (38.7, (-0.5, -2.05)), (38.9, (-1.0 + wave, 0.3)), (39.7, (-1.0 + wave, 0.3))])
    if standing:
        P["bag_at"] = "hand_r"
        P["hand_r"] = (1.4, -2.35)
    for k in ("open", "curl"):
        hi = (1.0 if k == "open" else 0.0)
        lo = (0.2 if k == "open" else 0.5)
        P["hand_l_" + k] = key(tc, [(0, lo), (5.8, lo), (6.0, hi), (6.6, hi), (6.8, lo), (11.3, lo), (11.7, hi), (13.3, hi), (13.7, lo),
                                    (34.4, lo), (34.8, hi), (37.0, hi), (37.4, lo), (38.7, lo), (38.9, hi)])
    return P, x, y


def ramesh_stop_pose(tc):
    """Shot 10: Ramesh alone at the bus stop."""
    P = dict(standing=True, bag_at="hand_r", hand_r=(1.4, -2.35), eye_open=blink(tc, [41.9, 44.0]))
    P["yaw"] = key(tc, [(39.8, 0.7), (42.0, 0.7), (42.4, 0.0)])
    P["look"] = key(tc, [(39.8, (0.9, 0.05)), (42.0, (0.9, 0.05)), (42.4, (0.0, 0.1))])
    wave = 0.2 * np.sin(tc * 13)
    P["hand_l"] = key(tc, [(39.8, (-1.4, -2.3)), (40.2, (-1.5 + wave, 0.35)), (41.6, (-1.5 + wave, 0.35)), (42.0, (-1.4, -2.3))])
    P["hand_l_open"] = key(tc, [(39.8, 0.2), (40.2, 1.0), (41.6, 1.0), (42.0, 0.2)])
    P["hand_l_curl"] = key(tc, [(39.8, 0.5), (40.2, 0.0), (41.6, 0.0), (42.0, 0.5)])
    P["smile"] = key(tc, [(39.8, 0.6), (42.4, 0.6), (42.8, 1.0)])
    P["brow"] = key(tc, [(39.8, 0.3), (42.4, 0.3), (42.7, 0.9)])            # "ನಾಳೆ… five lakh!"
    P["lid"] = key(tc, [(39.8, 0.1), (42.6, 0.1), (42.9, 0.35)])           # dreamy
    return P


# ------------------------------------------------------------------ screen-space extras
def money_bubble(t):
    """Daydream bubble over Suresh in his close-up, 25.0-28.8."""
    if not (25.0 <= t < 28.9):
        return VGroup()
    k = key(t, [(25.0, 0.0), (25.25, 1.12), (25.4, 1.0), (28.6, 1.0), (28.8, 0.0)])
    if k <= 0.01:
        return VGroup()
    cx, cy = -2.6, 2.0
    g = VGroup()
    puffs = [(0, 0, 1.6), (1.1, 0.3, 1.0), (-1.2, 0.35, 1.0), (0.6, 0.95, 0.9), (-0.6, 0.95, 0.9), (1.3, -0.55, 0.8),
             (-1.3, -0.5, 0.8), (0, -0.8, 0.9)]
    for dx, dy, r in puffs:
        g.add(Circle(radius=r).move_to(_p(cx + dx, cy + dy)).set_fill("#FFFDF6", 1).set_stroke(INK, 7))
    for dx, dy, r in puffs:                                 # inner fill over the inner strokes -> one cloud outline
        g.add(Circle(radius=r - 0.05).move_to(_p(cx + dx, cy + dy)).set_fill("#FFFDF6", 1).set_stroke(width=0))
    for i, (dx, dy, r) in enumerate([(0.9, -1.6, 0.22), (1.5, -2.1, 0.15)]):
        g.add(Circle(radius=r).move_to(_p(cx + dx, cy + dy)).set_fill("#FFFDF6", 1).set_stroke(INK, 6))
    rng = np.random.default_rng(5)
    for i in range(7):                                      # bundles of notes, bouncing
        bx = cx + rng.uniform(-1.3, 1.3)
        by = cy + rng.uniform(-0.6, 0.7) + 0.08 * np.sin(t * 8 + i)
        col = ("#7FBF7F", "#E7A6C6")[i % 2]
        ang = rng.uniform(-0.5, 0.5)
        note = blob([(-0.42, -0.2), (0.42, -0.2), (0.42, 0.2), (-0.42, 0.2)], col, smooth=False).rotate(ang)
        note.move_to(_p(bx, by))
        band = Rectangle(width=0.12, height=0.44).set_fill("#F5E6A8", 1).set_stroke(INK, 3).rotate(ang)
        band.move_to(note.get_center())
        g.add(note, band)
        g.add(Text("₹", font="DejaVu Sans", weight="BOLD", color=INK).scale(0.32).move_to(note.get_center() + _p(-0.22, 0)))
    g.scale(k, about_point=_p(cx + 1.5, cy - 2.1))
    return g


def headlight_sweep(t):
    """Bus leaving the stop: its light slides across the street to the right."""
    if not (39.8 <= t < 41.4):
        return VGroup()
    u = (t - 39.8) / 1.6
    x = -8 + 18 * u
    g = VGroup()
    for w, op in ((3.2, 0.06), (2.0, 0.08), (1.0, 0.08)):
        g.add(Polygon([x - w, 5, 0], [x + w, 5, 0], [x + w + 1.5, -5, 0], [x - w + 1.5, -5, 0]).set_fill("#FFE7A8", op).set_stroke(width=0))
    return g


# ------------------------------------------------------------------ scene
class Scene1(Scene):
    def construct(self):
        T = ValueTracker(0)
        img = lambda name, w=1.04: ImageMobject(str(HERE / "backdrops" / name)).scale_to_fit_width(config.frame_width * w)
        bg_street, bg_bus, bg_stop = img("b1_bus_road_night.png", 1.02), img("b2f_bus_front.png"), img("b3_bus_stop_night.png", 1.02)
        black = Rectangle(width=20, height=12).set_fill(BLACK, 1).set_stroke(width=0)

        def world():
            t = T.get_value()
            tc = np.floor(t * 12) / 12
            start, kind, cam = shot_at(t)
            g = Group()
            if kind == "street":
                z = key(t, [(0, 1.0), (3.5, 1.14)])
                g.add(bg_street.copy().scale(z, about_point=_p(0.6, -0.6)))
                g.shift(UP * 0.6 * shake(t))
            elif kind == "bus":
                d = dist(t)
                g.add(bg_bus.copy(), window_layer(d))
                rp, rx, ry = ramesh_pose(tc)
                sp, sx, sy = suresh_pose(tc)
                R = person(RAMESH, rp, t, x=rx, y=ry, s=1.18, seed=1)
                S = person(SURESH, sp, t, x=sx, y=sy, s=1.2, seed=2)
                if tc >= 38.4:
                    g.add(S, R)                 # Ramesh squeezes past in front of Suresh
                elif 4.7 <= tc:
                    g.add(R, S)
                else:
                    g.add(R)
                if speed(t) > 0.2:
                    g.add(light_sweep(d * 1.0))
                apply_cam(g, cam, t)
                g.shift(UP * shake(t))
            else:  # bus stop
                g.add(bg_stop.copy())
                g.add(person(RAMESH, ramesh_stop_pose(tc), t, x=-3.5, y=0.1, s=0.62, seed=3))
                g.add(headlight_sweep(t))
            g.add(money_bubble(t))
            fade = max(key(t, [(0, 1.0), (0.6, 0.0)]), key(t, [(44.5, 0.0), (45.5, 1.0)]))
            if fade > 0.001:
                g.add(black.copy().set_fill(opacity=fade))
            return g

        frame = Group()

        def rebuild(m):
            m.submobjects = list(world().submobjects)

        frame.add_updater(rebuild)
        rebuild(frame)
        self.add(frame)
        self.play(T.animate.set_value(DUR), run_time=DUR, rate_func=linear)

    def get_moving_and_static_mobjects(self, animations):
        return list(self.mobjects), []
