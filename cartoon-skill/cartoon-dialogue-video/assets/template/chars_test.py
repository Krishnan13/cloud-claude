import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from manim import *
from ink import person, puppy, RAMESH, SURESH, NEIGHBOUR, MADAM, crowd_spec

class Chars(Scene):
    def construct(self):
        self.camera.background_color = "#F3E3C3"
        t = 0.4
        self.add(person(MADAM, dict(yaw=0.3, smile=0.9, lid=0.45, hand_l=(-0.2, -1.45), hand_r=(0.45, -1.35), hand_l_curl=0.3, hand_r_curl=0.3), t, x=-4.6, y=-0.3, s=0.75))
        self.add(puppy(t, -4.45, -1.05, s=0.72, pose=dict(yaw=0.4, tongue=0.8)))
        self.add(person(NEIGHBOUR, dict(yaw=-0.6, smile=0.3, standing=True), t, x=-0.9, y=0.8, s=0.62))
        for i, xx in enumerate((1.6, 3.0, 4.4, 5.8)):
            self.add(person(crowd_spec(i), dict(back=True, standing=True, yaw=0.3 * (i % 2)), t, x=xx, y=0.5 + 0.1 * (i % 2), s=0.45 + 0.03 * i, seed=10 + i))
        self.add(person(RAMESH, dict(back=True, yaw=0.4), t, x=2.6, y=-2.6, s=0.7, seed=20))
