"""Style test: front two-shot in the bus, "living ink" characters.

    manim -qm -s --disable_caching style_test.py StyleFrame     # one still
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
from manim import *

from ink import person, RAMESH, SURESH, INK, blob

HERE = Path(__file__).resolve().parent
IMG_W, IMG_H = 1344, 768
K = config.frame_width / IMG_W            # scene units per backdrop pixel (cover width)


def px(x, y):
    return np.array([(x - IMG_W / 2) * K, (IMG_H / 2 - y) * K, 0.0])


# window glass of b2f_bus_front.png, in image pixels (measured on a grid)
WINDOW = [(52, 38), (440, 92), (432, 420), (72, 562)]
BARS = [((58, 62), (400, 118)), ((55, 160), (382, 178)), ((55, 245), (372, 238)),
        ((58, 335), (372, 300)), ((62, 430), (370, 362)), ((66, 515), (360, 410))]


def window_layer(t, speed=1.0):
    """Night street seen through the window: lights slide past behind the grill bars."""
    g = VGroup()
    glass = Polygon(*[px(*p) for p in WINDOW]).set_fill("#0E1830", 1).set_stroke(width=0)
    g.add(glass)
    x0, x1 = px(*WINDOW[0])[0], px(*WINDOW[1])[0]
    rng = np.random.default_rng(3)
    lamps = [(rng.uniform(0, 1), rng.uniform(0.15, 0.85), rng.uniform(0.6, 1.4)) for _ in range(9)]
    span = x1 - x0 + 2.0
    for u, v, sz in lamps:
        # characters face the front of the bus (towards camera), so the street slides from the
        # near (left) end of the window to the far (right) end
        x = x0 - 1.0 + ((u * span + t * 2.6 * speed * (0.7 + 0.3 * sz)) % span)
        top = px(*WINDOW[0])[1] + (px(*WINDOW[1])[1] - px(*WINDOW[0])[1]) * (x - x0) / (x1 - x0)
        bot = px(*WINDOW[3])[1] + (px(*WINDOW[2])[1] - px(*WINDOW[3])[1]) * (x - x0) / (x1 - x0)
        y = bot + (top - bot) * v
        for r, op in ((0.32 * sz, 0.10), (0.18 * sz, 0.25), (0.07 * sz, 0.9)):
            g.add(Circle(radius=r).move_to([x, y, 0]).set_fill("#FFB347", op).set_stroke(width=0))
    g.add(Polygon(*[px(*p) for p in WINDOW]).set_fill(opacity=0).set_stroke(INK, 8))
    for a, b in BARS:
        g.add(Line(px(*a), px(*b), stroke_width=16, color=INK))
        g.add(Line(px(*a), px(*b), stroke_width=9, color="#9AA6B2"))
    return g


def light_sweep(t, period=3.2):
    """A warm street-light band sliding across the people (bus moving)."""
    u = (t % period) / period
    x = -12 + 24 * u
    g = VGroup()
    for w, op in ((2.6, 0.05), (1.6, 0.06), (0.8, 0.06)):
        g.add(Polygon([x - w, 5, 0], [x + w * 0.4, 5, 0], [x + 1.6 + w * 0.4, -5, 0], [x + 1.6 - w, -5, 0])
              .set_fill("#FFC46B", op).set_stroke(width=0))
    return g


class StyleFrame(Scene):
    def construct(self):
        t = 1.15
        bg = ImageMobject(str(HERE / "backdrops/b2f_bus_front.png"))
        bg.scale_to_fit_width(config.frame_width)
        self.add(window_layer(t), bg)
        # the backdrop's own window is replaced: cut it out by drawing our window over the backdrop
        self.add(window_layer(t))
        ram = dict(yaw=0.85, smile=0.65, look=(0.9, 0.05), brow=0.15, tilt=0.25)
        sur = dict(yaw=-0.85, mouth=0.55, smile=0.5, brow=0.45, look=(-0.85, 0.05),
                   hand_l=(-1.75, -1.0), hand_l_dir=2.0, hand_l_open=1.0, hand_l_curl=0.0,
                   lean=-0.12, tilt=-0.4)
        self.add(person(RAMESH, ram, t, x=-2.65, y=-0.6, s=1.18, seed=1))
        self.add(person(SURESH, sur, t, x=2.55, y=-0.55, s=1.2, seed=2))
        self.add(light_sweep(t))
