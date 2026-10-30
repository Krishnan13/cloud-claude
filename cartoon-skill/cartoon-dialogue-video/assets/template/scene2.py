"""Scene 2 — next morning: the crowd, the news, the window, the puppy. 38 s.

    manim -qm --frame_rate 24 --disable_caching scene2.py Scene2
Motion is chosen to suit each flat backdrop:
  lane   — the lane runs towards camera, so the friends walk TOWARDS us (grow as they come)
  gate   — crowd seen from behind; friends enter from the side
  talk   — zoomed gate plate behind waist-up characters
  peek   — backs of their heads rise into the window
  reveal — living room seen through bars drawn in front
  faces  — reverse shot: their faces behind the bars, outside blurred
  sting  — freeze, slow push, "ಯಬೂಊಊ"
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
from manim import *

from ink import person, puppy, hand, RAMESH as _R, SURESH as _S, NEIGHBOUR, MADAM, crowd_spec, INK, _p
from envelope import voice_envelope, mouth_at
from scene1 import key, blink, ease
from style_test import HERE

RAMESH, SURESH = dict(_R, bag=None), dict(_S, bag=None)     # no shopping bags the next morning
DUR = 38.0
STING_AT = 33.3                  # Suresh says the catchphrase, THEN the picture freezes
FREEZE = 35.7
LINES = {"n1": ("n1_neighbour.mp3", 13.6), "so": ("o_suresh.mp3", 15.9), "ro": ("o_ramesh.mp3", 16.05),
         "sy": ("sting_yabuu.mp3", STING_AT)}
ENV = {k: (voice_envelope(str(HERE / "audio" / f)), t0) for k, (f, t0) in LINES.items()}


def talk(k, t):
    env, t0 = ENV[k]
    return mouth_at(env, t - t0)


SHOTS = [(0.0, "lane"), (7.0, "gate"), (11.5, "talk"), (19.0, "window"), (20.2, "peek"), (24.0, "reveal"), (29.5, "faces"), (FREEZE, "sting")]


def shot_at(t):
    cur = SHOTS[0]
    for s in SHOTS:
        if t >= s[0]:
            cur = s
    return cur


def bars(xs, wood="#5B3A22", width=0.42, frame=True):
    """Wooden window bars (and frame) drawn in front of the camera."""
    g = VGroup()
    for x in xs:
        g.add(Rectangle(width=width, height=9.0).move_to(_p(x, 0)).set_fill(wood, 1).set_stroke(INK, 8))
        g.add(Line(_p(x - width * 0.22, 4.4), _p(x - width * 0.22, -4.4), stroke_width=4, color="#8A6040"))
    if frame:
        for (cx, cy, w, h) in ((0, 4.25, 16, 1.2), (0, -4.25, 16, 1.2), (-7.45, 0, 1.3, 9), (7.45, 0, 1.3, 9)):
            g.add(Rectangle(width=w, height=h).move_to(_p(cx, cy)).set_fill("#4A2E1A", 1).set_stroke(INK, 10))
    return g


# ------------------------------------------------------------------ acting per shot
def lane(tc, t):
    """Side view: they walk along the wall SEARCHING for the child, then hear the crowd and hurry on."""
    FEET, S = -3.25, 0.6
    out = []
    for spec, lead, seed in ((RAMESH, 0.0, 1), (SURESH, 1.7, 2)):
        stop1 = key(tc, [(3.0, 1.0), (3.25, 0.0), (4.3, 0.0), (4.55, 1.0)])      # pause to search
        stop2 = key(tc, [(5.4, 1.0), (5.6, 0.0), (6.3, 0.0), (6.45, 1.6)])        # freeze: the crowd! then hurry
        walk = min(stop1, stop2)
        x = key(tc, [(0.4, -8.6), (3.0, -3.9), (4.3, -3.9), (5.4, -1.6), (6.3, -1.6), (7.0, 2.4)]) - lead
        ph = tc * 8.5 + (0 if spec is RAMESH else 1.4)
        P = dict(side=1, walk=min(walk, 1.0), phase=ph, smile=0.4, eye_open=blink(tc, [1.7 + lead * 0.3, 4.9]))
        if spec is RAMESH:
            # looks over the wall, then bends to peer into the bush
            P["yaw"] = key(tc, [(0, 1.0), (1.2, 1.0), (1.4, 0.3), (2.2, 0.3), (2.4, 1.0), (5.6, 1.0), (5.8, 0.75)])
            P["look"] = key(tc, [(0, (0.9, 0.0)), (1.2, (0.9, 0.0)), (1.4, (0.0, 0.8)), (2.2, (0.0, 0.8)), (2.4, (0.9, 0.0)),
                                 (3.3, (0.9, -0.7)), (4.2, (0.9, -0.7)), (4.4, (0.9, 0.0))])
            P["tilt"] = key(tc, [(3.2, 0.0), (3.5, 0.9), (4.2, 0.9), (4.4, 0.0)])
            P["brow"] = key(tc, [(0, 0.3), (5.55, 0.3), (5.7, 1.0)])
            P["wide"] = key(tc, [(5.55, 0.0), (5.7, 0.9), (6.4, 0.6)])
        else:
            # hand shading his eyes, scanning; then points at the crowd
            shade = key(tc, [(1.8, 0.0), (2.0, 1.0), (3.0, 1.0), (3.2, 0.0)])
            if shade > 0.5:
                P["hand_near"] = (0.75, 1.5)
            if 5.75 < tc < 6.35:
                P["hand_near"], P["open_near"] = (2.1, 0.2), 0.9
            P["yaw"] = key(tc, [(0, 1.0), (3.3, 1.0), (3.5, 0.2), (4.2, 0.2), (4.4, 1.0)])
            P["look"] = key(tc, [(0, (0.9, 0.05)), (3.3, (0.9, 0.05)), (3.5, (-0.3, 0.3)), (4.2, (-0.3, 0.3)), (4.4, (0.9, 0.05))])
            P["brow"] = key(tc, [(0, 0.5), (5.6, 0.5), (5.75, 1.0)])
            P["wide"] = key(tc, [(5.6, 0.0), (5.75, 0.8)])
        out.append(person(spec, P, t, x=x, y=FEET + 4.85 * S, s=S, seed=seed))
    return out


CROWD = [(-2.1, 0.43, 0), (-1.25, 0.46, 1), (-0.35, 0.42, 2), (0.5, 0.47, 3), (1.35, 0.44, 4), (2.15, 0.41, 5)]


def crowd(t, tc):
    g = []
    for x, s, i in CROWD:
        P = dict(back=True, standing=True, yaw=0.35 * np.sin(tc * 0.9 + i * 1.7), hand_l=(-1.35, -2.3), hand_r=(1.35, -2.3))
        g.append(person(crowd_spec(i), P, t, x=x + 0.05 * np.sin(tc + i), y=-3.25 + 4.85 * s, s=s, seed=30 + i))
    return g


def gate(tc, t):
    out = []
    for spec, x_end, seed, delay in ((RAMESH, -4.6, 1, 0.0), (SURESH, -2.7, 2, 0.25)):
        x = key(tc, [(7.2 + delay, -9.5), (8.9 + delay, x_end)])
        walking = 7.2 + delay < tc < 8.9 + delay
        tip = key(tc, [(9.5, 0.0), (9.8, 0.25), (10.5, 0.25), (10.8, 0.0)])     # on tiptoe to see over
        P = dict(back=True, standing=True, stride=np.sin(tc * 9) if walking else 0.0,
                 yaw=key(tc, [(0, 0.0), (10.8, 0.0), (11.0, 0.5 if spec is RAMESH else -0.5)]),
                 hand_l=(-1.35, -2.3), hand_r=(1.35, -2.3))
        y = -4.9 + 4.85 * 0.66 + tip + (0.05 * abs(np.sin(tc * 9)) if walking else 0)
        out.append(person(spec, P, t, x=x, y=y, s=0.66, seed=seed))
    return out


def talk_shot(tc, t):
    m_n, m_s, m_r = talk("n1", tc), talk("so", tc), talk("ro", tc)
    fall = key(tc, [(15.8, 0.0), (16.2, 1.0)])                    # the news lands: faces fall
    look_each = key(tc, [(17.6, 0.0), (17.9, 1.0)])
    # Suresh (middle), taps the neighbour
    tap = 0.12 * np.sin(tc * 30) if 11.8 < tc < 12.2 else 0.0
    sp = dict(standing=True, yaw=key(tc, [(0, 0.7), (17.6, 0.7), (17.9, -0.75)]), look=(0.9, 0.0) if look_each < 0.5 else (-0.9, 0.0),
              mouth=m_s, brow=0.5 * (1 - fall) - 0.1 * fall, worry=0.9 * fall, lid=0.1 + 0.4 * fall, smile=0.5 - 1.1 * fall,
              eye_open=blink(tc, [14.2, 18.4]),
              hand_r=key(tc, [(11.5, (1.3, -2.3)), (11.75, (2.05 + tap, -0.55)), (12.25, (2.05 + tap, -0.55)), (12.5, (1.3, -2.3))]),
              hand_r_open=key(tc, [(11.5, 0.2), (11.75, 0.6), (12.25, 0.6), (12.5, 0.2)]),
              hand_r_curl=key(tc, [(11.5, 0.5), (11.75, 0.1), (12.25, 0.1), (12.5, 0.5)]),
              bob=-0.15 * fall, tilt=key(tc, [(18.0, 0.0), (18.3, 0.5), (18.6, 0.0)]))
    # Ramesh (left): palms up "what happened?"
    rp = dict(standing=True, yaw=key(tc, [(0, 0.6), (17.6, 0.6), (17.9, 0.8)]), look=(0.9, 0.0),
              mouth=m_r, brow=key(tc, [(12.5, 0.2), (12.7, 0.8), (15.8, 0.8)]) * (1 - fall) - 0.1 * fall, worry=0.9 * fall,
              lid=0.1 + 0.4 * fall, smile=0.4 - 1.0 * fall, eye_open=blink(tc, [13.0, 17.2]), bob=-0.15 * fall,
              hand_l=key(tc, [(12.4, (-1.35, -2.3)), (12.7, (-1.5, -1.2)), (13.6, (-1.5, -1.2)), (13.9, (-1.35, -2.3))]),
              hand_r=key(tc, [(12.4, (1.35, -2.3)), (12.7, (1.5, -1.2)), (13.6, (1.5, -1.2)), (13.9, (1.35, -2.3))]),
              hand_l_open=key(tc, [(12.4, 0.2), (12.7, 1.0), (13.6, 1.0), (13.9, 0.2)]),
              hand_r_open=key(tc, [(12.4, 0.2), (12.7, 1.0), (13.6, 1.0), (13.9, 0.2)]),
              hand_l_curl=key(tc, [(12.4, 0.5), (12.7, 0.0), (13.6, 0.0), (13.9, 0.5)]),
              hand_r_curl=key(tc, [(12.4, 0.5), (12.7, 0.0), (13.6, 0.0), (13.9, 0.5)]),
              hand_l_dir=key(tc, [(12.4, -1.6), (12.7, 1.9), (13.6, 1.9), (13.9, -1.6)]),
              hand_r_dir=key(tc, [(12.4, -1.6), (12.7, 1.2), (13.6, 1.2), (13.9, -1.6)]))
    # neighbour (right): watching the house, turns, says it casually with a thumb over his shoulder
    turned = tc >= 12.2
    npose = dict(standing=True, back=not turned, yaw=key(tc, [(12.2, -0.2), (12.5, -0.65)]), look=(-0.9, 0.0),
                 mouth=m_n, smile=0.35, brow=key(tc, [(13.5, 0.2), (13.7, 0.6), (15.4, 0.2)]), eye_open=blink(tc, [14.9, 17.7]),
                 hand_r=key(tc, [(13.4, (1.35, -2.3)), (13.7, (1.5, 0.25)), (15.3, (1.5, 0.25)), (15.6, (1.35, -2.3))]),
                 hand_r_dir=0.5, hand_r_curl=0.7, hand_l=(-1.35, -2.3),
                 tilt=key(tc, [(13.6, 0.0), (14.0, 0.3), (15.3, 0.3), (15.6, 0.0)]))
    return [person(RAMESH, rp, t, x=-3.7, y=-0.25, s=0.95, seed=1),
            person(SURESH, sp, t, x=-0.35, y=-0.3, s=0.97, seed=2),
            person(NEIGHBOUR, npose, t, x=3.5, y=-0.15, s=0.92, seed=5)]


SILL = -2.45                     # top of the window sill, seen from inside the house
FACE_X = {"r": -2.35, "s": 2.15}
FACE_S = 1.12
FACE_Y = -1.2                    # neck height once they have risen into the window


def sill_hands(t, who_rise):
    """Fingers curled over the sill, drawn in front of it."""
    g = VGroup()
    for spec, k, r in who_rise:
        if r < 0.95:
            continue
        x = FACE_X[k]
        for side in (-1, 1):
            g.add(hand((x + side * 0.95, SILL + 0.12), -1.57, spec["skin"], spread=0.4, curl=0.35).scale(FACE_S))
    return g


def peek(tc, t):
    """Their faces rise slowly from below the sill, eyes searching the room."""
    out, rises = [], []
    for spec, k, seed, d in ((RAMESH, "r", 1, 0.0), (SURESH, "s", 2, 0.25)):
        r = key(tc, [(20.5 + d, 0.0), (22.0 + d, 1.0)])
        search = key(tc, [(22.2, (-0.6, 0.0)), (22.8, (0.6, 0.0)), (23.3, (-0.3, 0.0)), (23.7, (0.0, -0.05))])
        P = dict(standing=True, yaw=0.0, look=search, wide=key(tc, [(20.5, 0.2), (23.7, 0.2), (23.9, 0.8)]),
                 brow=key(tc, [(20.5, 0.4), (23.7, 0.4), (23.9, 0.9)]), smile=0.2, lid=0.05,
                 eye_open=blink(tc, [22.9 + d]), hand_l=(-1.35, -2.3), hand_r=(1.35, -2.3))
        out.append(person(spec, P, t, x=FACE_X[k], y=FACE_Y - 3.6 * (1 - r), s=FACE_S, seed=seed))
        rises.append((spec, k, r))
    return out, rises


def reveal(tc, t):
    rock = np.sin(tc * 2.2)
    kiss = sum(np.exp(-((tc - c) / 0.25) ** 2) for c in (25.3, 26.9))
    P = dict(yaw=0.25 + 0.15 * rock + 0.25 * kiss, smile=1.0, lid=0.5 - 0.3 * kiss, tilt=0.4 * rock + 0.5 * kiss,
             mouth=0.15 * kiss, hand_l=(-0.2, -1.45), hand_r=(0.45, -1.35), hand_l_curl=0.3, hand_r_curl=0.3,
             lean=0.08 * rock, eye_open=blink(tc, [28.1]))
    mx, my, ms = -1.33, 0.12, 0.8
    madam = person(MADAM, P, t, x=mx, y=my, s=ms, seed=6)
    yip = sum(np.exp(-((tc - c) / 0.12) ** 2) for c in (24.4, 26.1, 28.4))
    pup = puppy(t, mx + 0.12 * ms + 0.08 * ms * rock, my - 0.85 * ms, s=0.6,
                pose=dict(yaw=0.3 * np.sin(tc * 1.3), tongue=0.3 + 0.7 * yip, wag=1.0))
    return [madam, pup]


def faces(tc, t):
    turn = key(tc, [(30.9, 0.0), (31.9, 1.0)])          # slowly turn to each other
    out = []
    for spec, k, sg, seed in ((RAMESH, "r", 1, 1), (SURESH, "s", -1, 2)):
        P = dict(standing=True, yaw=0.85 * sg * turn, look=(0.9 * sg * turn, 0.05 * (1 - turn)),
                 lid=0.55, mouth=0.0, smile=-0.15, brow=-0.15, eye_open=blink(tc, [30.2 if sg > 0 else 30.4]),
                 hand_l=(-1.35, -2.3), hand_r=(1.35, -2.3))
        if spec is SURESH:              # "ಯಬೂಊಊ": puzzled and amused, one brow up, a little head tilt
            say = key(tc, [(STING_AT - 0.2, 0.0), (STING_AT, 1.0)])
            P.update(mouth=talk("sy", tc), lid=0.55 - 0.3 * say, smile=-0.15 + 0.45 * say, brow=-0.15 + 0.6 * say,
                     worry=0.35 * say, tilt=-0.35 * say)
        out.append(person(spec, P, t, x=FACE_X[k], y=FACE_Y, s=FACE_S, seed=seed))
    return out, [(RAMESH, "r", 1.0), (SURESH, "s", 1.0)]


def inside_window(bg, chars, rises, t):
    """Camera inside the house looking out: blurred lane, faces, wall + sill, bars, fingers on the sill."""
    g = Group(bg, *chars)
    g.add(Rectangle(width=16, height=2.2).move_to(_p(0, SILL - 1.15)).set_fill("#EADFC8", 1).set_stroke(width=0))
    g.add(bars([-4.7, -0.1, 4.5], frame=True))
    g.add(Rectangle(width=16, height=0.5).move_to(_p(0, SILL - 0.18)).set_fill("#6B4428", 1).set_stroke(INK, 9))
    g.add(Line(_p(-8, SILL - 0.08), _p(8, SILL - 0.08), stroke_width=4, color="#9A6A44"))
    g.add(sill_hands(t, rises))
    return g


# ------------------------------------------------------------------ scene
class Scene2(Scene):
    def construct(self):
        T = ValueTracker(0)
        img = lambda name, w=1.02: ImageMobject(str(HERE / "backdrops" / name)).scale_to_fit_width(config.frame_width * w)
        bgs = {k: img(f) for k, f in (("lane", "b7_lane_side.png"), ("gate", "b4_house_gate.png"), ("peek", "b5_window_outside.png"),
                                       ("reveal", "b6_living_room.png"), ("faces", "b0_lane_blur.png"))}
        black = Rectangle(width=20, height=12).set_fill(BLACK, 1).set_stroke(width=0)
        dawn = Rectangle(width=20, height=12).set_fill("#22345E", 1).set_stroke(width=0)

        def world(t):
            tc = np.floor(t * 12) / 12
            start, kind = shot_at(t)
            g = Group()
            if kind == "lane":
                g.add(bgs["lane"].copy(), *lane(tc, t))
                g.add(dawn.copy().set_fill(opacity=0.7 * (1 - ease(key(t, [(0.2, 0.0), (1.8, 1.0)])))))
            elif kind == "gate":
                g.add(bgs["gate"].copy(), *crowd(t, tc), *gate(tc, t))
            elif kind == "talk":
                bg = bgs["gate"].copy().scale(1.75, about_point=_p(-0.2, -1.9)).shift(_p(1.1, 0.9))
                g.add(bg, *talk_shot(tc, t))
            elif kind == "window":                     # "that window": 1.2 s establishing push-in
                g.add(bgs["peek"].copy().scale(key(t, [(19.0, 1.0), (20.2, 1.08)]), about_point=_p(-1.6, 0.4)))
            elif kind == "peek":
                chars, rises = peek(tc, t)
                g.add(inside_window(bgs["faces"].copy(), chars, rises, t))
                g.scale(key(t, [(20.2, 1.0), (24.0, 1.06)]), about_point=_p(0, 0.3))
            elif kind == "reveal":
                z = key(t, [(24.0, 1.15), (29.5, 1.62)])
                inner = Group(bgs["reveal"].copy(), *reveal(tc, t)).scale(z, about_point=_p(-1.25, -0.2)).shift(_p(1.25, -0.35))
                g.add(inner, bars([-5.2, -3.4, 0.9, 2.9, 4.9]))
            else:  # faces (and the sting freezes this shot)
                tf = min(t, FREEZE)
                tcf = np.floor(tf * 12) / 12
                chars, rises = faces(tcf, tf)
                g.add(inside_window(bgs["faces"].copy(), chars, rises, tf))
                if kind == "sting":
                    g.scale(key(t, [(FREEZE, 1.0), (36.4, 1.14)]), about_point=_p(0, 0.6))
            fade = max(key(t, [(0, 1.0), (0.5, 0.0)]), key(t, [(37.2, 0.0), (38.0, 1.0)]))
            if fade > 0.001:
                g.add(black.copy().set_fill(opacity=fade))
            return g

        frame = Group()

        def rebuild(m):
            m.submobjects = list(world(T.get_value()).submobjects)

        frame.add_updater(rebuild)
        rebuild(frame)
        self.add(frame)
        self.play(T.animate.set_value(DUR), run_time=DUR, rate_func=linear)

    def get_moving_and_static_mobjects(self, animations):
        return list(self.mobjects), []
