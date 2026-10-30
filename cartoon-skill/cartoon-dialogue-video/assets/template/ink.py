"""ink.py -- the "living ink cartoon" character style.

Big heads, bold black outlines, flat colour, lines that boil (re-jitter) a few
times per second so the drawing feels hand-made. Characters are rebuilt from a
pose dict every frame; nothing here keeps state.

    person(spec, pose, t)  ->  VGroup

`spec` = who it is (colours, hair, moustache...). `pose` = what they are doing
right now (head yaw, mouth, brows, hands...). Every pose key is optional.
"""
import numpy as np
from manim import (VGroup, VMobject, Ellipse, Circle, Line, Text, Polygon,
                   CapStyleType, LEFT, RIGHT, UP, DOWN)

INK = "#20140E"
OL = 7            # outline stroke width (Manim units: 100 = 1 scene unit)
BOIL_FPS = 8      # how many times a second the lines re-wobble
BOIL_AMP = 0.010  # wobble size in scene units

RAMESH = dict(skin="#B7764A", shade="#9A5F38", shirt="#5A3A28", shirt_dark="#43291B",
              pants="#C8873F", hair="partline", moustache=True, stubble=False,
              tilak=True, collar="polo", bag="#5B8FD0", bag_text=None)
SURESH = dict(skin="#A86A40", shade="#8C5432", shirt="#6E9DAE", shirt_dark="#557F8E",
              pants="#4A4A52", hair="spiky", moustache=False, stubble=True,
              tilak=False, collar="crew", bag="#F2E27A", bag_text="S.K. TEXTILES")

NEIGHBOUR = dict(skin="#A46A44", shade="#8A5636", shirt="#F1EEE4", shirt_dark="#D6D2C4", pants="#ECE8DC",
                 hair="partline", hair_color="#D9D6CF", moustache=True, stubble=False, tilak=False,
                 collar="polo", glasses=True, bag=None, bag_text=None)
MADAM = dict(skin="#C08155", shade="#A46A44", shirt="#7A2E5A", shirt_dark="#5E2246", pants="#C2185B",
             hair="bun", moustache=False, stubble=False, tilak=False, bindi=True, collar="crew",
             saree="#E0457B", saree_border="#F2C14E", earrings=True, bag=None, bag_text=None)


def crowd_spec(i):
    """Neighbours for the crowd at the gate (seen from behind)."""
    shirts = ["#E8E2D0", "#8E5B3A", "#3E6E8E", "#B84A4A", "#6B7F3A", "#D8A23A", "#5B4A8A"]
    hairs = ["partline", "bun", "spiky", "partline", "bun", "partline", "spiky"]
    hc = ["#1A1410", "#1A1410", "#2A2018", "#C9C6BF", "#1A1410", "#3A2A20", "#1A1410"]
    return dict(skin="#A86A40", shade="#8C5432", shirt=shirts[i % 7], shirt_dark=shirts[i % 7], pants="#4A4A52",
                hair=hairs[i % 7], hair_color=hc[i % 7], moustache=False, collar="crew", bag=None, bag_text=None)


def _p(x, y):
    return np.array([x, y, 0.0])


def blob(pts, fill, stroke=INK, sw=OL, smooth=True, opacity=1.0):
    pts = [_p(*q) for q in pts]
    m = VMobject()
    if smooth:
        m.set_points_smoothly(pts + [pts[0]])
    else:
        m.set_points_as_corners(pts + [pts[0]])
    m.set_fill(fill, opacity=opacity).set_stroke(stroke, sw)
    return m


def curve(pts, sw=OL, color=INK):
    m = VMobject()
    m.set_points_smoothly([_p(*q) for q in pts])
    m.set_stroke(color, sw).set_fill(opacity=0)
    return m


def limb(a, b, width, color):
    """A rounded limb: thick black line with a slightly thinner coloured line on top."""
    out = Line(_p(*a), _p(*b), stroke_width=width * 100 + 2 * OL, color=INK)
    inn = Line(_p(*a), _p(*b), stroke_width=width * 100, color=color)
    for m in (out, inn):
        m.set_cap_style(CapStyleType.ROUND)
    return VGroup(out, inn)


def ik(shoulder, hand, l1, l2, bend):
    """Two-bone arm: returns elbow position. bend=+1 elbow out to the right, -1 to the left."""
    s, h = np.array(shoulder, float), np.array(hand, float)
    d = h - s
    dist = min(np.linalg.norm(d), l1 + l2 - 1e-3)
    d = d / (np.linalg.norm(d) + 1e-9)
    a = (l1 ** 2 - l2 ** 2 + dist ** 2) / (2 * dist)
    hgt = np.sqrt(max(l1 ** 2 - a ** 2, 0))
    perp = np.array([-d[1], d[0]]) * bend
    return s + d * a + perp * hgt


def hand(c, direction, skin, spread=0.5, curl=0.0):
    """Cartoon hand: palm + four fingers + thumb. direction = where the fingers point (radians).
    spread 0..1 fans the fingers open; curl 0..1 shortens them (holding something)."""
    g = VGroup()
    c = np.array(c, float)
    u = np.array([np.cos(direction), np.sin(direction)])
    v = np.array([-u[1], u[0]])
    flen = 0.2 * (1 - 0.55 * curl)
    for i, k in enumerate((-1.5, -0.5, 0.5, 1.5)):
        base = c + u * 0.1 + v * k * 0.065
        ang = direction + k * 0.16 * spread
        tip = base + np.array([np.cos(ang), np.sin(ang)]) * flen * (0.85 if abs(k) > 1 else 1.0)
        g.add(limb(base, tip, 0.085, skin))
    thumb_base = c + v * 0.11
    ta = direction + 1.1 + 0.4 * spread
    g.add(limb(thumb_base, thumb_base + np.array([np.cos(ta), np.sin(ta)]) * 0.15, 0.09, skin))
    palm = Ellipse(width=0.34, height=0.3).rotate(direction).move_to(_p(*c)).set_fill(skin, 1).set_stroke(INK, OL)
    g.add(palm)
    return g


def boil(group, t, seed):
    """Wobble the drawing a little, changing BOIL_FPS times a second.

    The offset is a smooth field of position, so points that touch (curve joins,
    closed shapes) move together and fills stay intact.
    """
    step = int(t * BOIL_FPS)
    rng = np.random.default_rng((seed * 7919 + step * 104729) % (2 ** 32))
    waves = [(rng.uniform(2, 5, 2) * rng.choice([-1, 1], 2), rng.uniform(0, 2 * np.pi, 2)) for _ in range(3)]
    for m in group.family_members_with_points():
        if getattr(m, "no_boil", False):
            continue
        p = m.points
        off = np.zeros_like(p)
        for (k, ph) in waves:
            off[:, 0] += np.sin(k[0] * p[:, 0] + k[1] * p[:, 1] + ph[0])
            off[:, 1] += np.sin(k[1] * p[:, 0] - k[0] * p[:, 1] + ph[1])
        m.points = p + off * (BOIL_AMP / np.sqrt(len(waves)))
    return group


# ---------------------------------------------------------------- head parts
def eye(cx, cy, w, h, openness, look, wide, skin, lid=0.3):
    """Cartoon eye: white, big dark pupil, and an upper eyelid (lid 0 = wide open, 1 = closed)."""
    g = VGroup()
    lid = float(np.clip(lid - 0.35 * wide, 0, 1))
    if openness < 0.15 or lid > 0.92:
        g.add(curve([(cx - w / 2, cy), (cx, cy - 0.035), (cx + w / 2, cy)], sw=OL * 1.1))
        return g
    hh = h * (1 + 0.25 * wide)
    ww = w * (1 + 0.15 * wide)
    g.add(Ellipse(width=ww, height=hh).move_to(_p(cx, cy)).set_fill("#FFFDF6", 1).set_stroke(INK, OL * 0.8))
    r = min(0.1 * (1 - 0.25 * wide), ww * 0.42)
    px = cx + look[0] * max(ww / 2 - r - 0.015, 0)
    py = cy + look[1] * max(hh / 2 - r - 0.015, 0)
    g.add(Circle(radius=r).move_to(_p(px, py)).set_fill("#2A1A12", 1).set_stroke(width=0))
    g.add(Circle(radius=r * 0.3).move_to(_p(px + r * 0.35, py + r * 0.38)).set_fill("#FFFFFF", 1).set_stroke(width=0))
    # upper lid: skin cap over the top of the eye with a firm lash line (also used for blinks)
    cover = min(lid + (1 - openness), 1.0)
    if cover > 0.04:
        ly = cy + hh / 2 - hh * cover
        cap = [(cx - ww * 0.56, cy + hh * 0.62), (cx + ww * 0.56, cy + hh * 0.62), (cx + ww * 0.56, ly - 0.02), (cx, ly + 0.03), (cx - ww * 0.56, ly - 0.02)]
        g.add(blob(cap, skin, sw=0))
        g.add(curve([(cx - ww * 0.5, ly - 0.03), (cx, ly + 0.03), (cx + ww * 0.5, ly - 0.03)], sw=OL * 1.1))
    return g


def mouth(cx, cy, w, openness, smile):
    if openness < 0.08:
        k = 0.07 * smile
        return VGroup(curve([(cx - w / 2, cy + k), (cx, cy - k * 0.6), (cx + w / 2, cy + k)], sw=OL))
    h = 0.06 + 0.34 * openness
    up = 0.05 * smile
    outline = [(cx - w / 2, cy + up), (cx - w * 0.25, cy + 0.03), (cx, cy + 0.02), (cx + w * 0.25, cy + 0.03),
               (cx + w / 2, cy + up), (cx + w * 0.3, cy - h * 0.8), (cx, cy - h), (cx - w * 0.3, cy - h * 0.8)]
    g = VGroup(blob(outline, "#4A1612", sw=OL * 0.9))
    if openness > 0.35:
        g.add(Ellipse(width=w * 0.5, height=h * 0.45).move_to(_p(cx, cy - h * 0.72)).set_fill("#D9534F", 1).set_stroke(width=0))
    if openness > 0.2:
        g.add(blob([(cx - w * 0.32, cy + 0.0), (cx + w * 0.32, cy + 0.0), (cx + w * 0.26, cy - 0.07), (cx - w * 0.26, cy - 0.07)],
                   "#FFFDF6", sw=0, smooth=False))
    return g


def head(spec, P, ox, oy):
    """P = pose; ox, oy = head centre."""
    yaw = P.get("yaw", 0.0)
    HW, HH = 0.80, 0.95                    # half width / half height (big head)
    fx = ox + 0.55 * yaw * HW              # where the face features sit (strong 3/4 turn)
    sg, ay = (1 if yaw >= 0 else -1), abs(yaw)
    g = VGroup()

    if spec["hair"] == "bun":                       # bun sits behind the head, a little to the back side
        g.add(Circle(radius=0.34).move_to(_p(ox - 0.35 * yaw, oy + HH * 0.98)).set_fill(spec.get("hair_color", "#1A1410"), 1).set_stroke(INK, OL))
    # ears (the one on the turning side tucks away)
    for side in (-1, 1):
        k = 1 - 2.2 * max(0.0, side * yaw)           # ear on the turning side hides fast
        if k > 0.15:
            ex = ox + side * HW * 0.97 + 0.12 * yaw     # back ear slides a little towards the middle
            g.add(Ellipse(width=0.26 * k, height=0.38).move_to(_p(ex, oy - 0.05)).set_fill(spec["skin"], 1).set_stroke(INK, OL))

    chin = 0.32 * yaw
    out_ = lambda side: HW * (1 + (0.07 if side == sg else -0.06) * ay)   # cheek bulges on the turning side
    face = [(ox - out_(-1), oy + 0.15), (ox - out_(-1) * 0.85, oy + HH * 0.75), (ox + 0.08 * yaw, oy + HH),
            (ox + out_(1) * 0.85, oy + HH * 0.75), (ox + out_(1), oy + 0.15), (ox + out_(1) * 0.8 + chin * 0.4, oy - HH * 0.6),
            (ox + chin, oy - HH), (ox - out_(-1) * 0.8 + chin * 0.4, oy - HH * 0.6)]
    g.add(blob(face, spec["skin"]))
    if spec.get("stubble"):
        jaw = [(ox - HW * 0.78 + chin * 0.3, oy - HH * 0.35), (fx - 0.35, oy - HH * 0.45), (fx, oy - HH * 0.5),
               (fx + 0.35, oy - HH * 0.45), (ox + HW * 0.78 + chin * 0.3, oy - HH * 0.35),
               (ox + HW * 0.7 + chin * 0.3, oy - HH * 0.65), (ox + chin, oy - HH * 0.98), (ox - HW * 0.7 + chin * 0.3, oy - HH * 0.65)]
        g.add(blob(jaw, spec["shade"], sw=0, opacity=0.55))

    # hair cap
    part = -0.3 * yaw
    if spec["hair"] == "bun":                       # smooth hair, centre parting, covering the ears' tops
        hair = [(ox - HW * 1.08, oy - 0.3), (ox - HW * 1.02, oy + HH * 0.85), (ox + part, oy + HH * 1.1),
                (ox + HW * 1.02, oy + HH * 0.85), (ox + HW * 1.08, oy - 0.3), (ox + HW * 0.9, oy - 0.25), (ox + HW * 0.82, oy + HH * 0.45),
                (ox + 0.25 + part, oy + HH * 0.78), (ox + part, oy + HH * 0.72), (ox - 0.25 + part, oy + HH * 0.78),
                (ox - HW * 0.82, oy + HH * 0.45), (ox - HW * 0.9, oy - 0.25)]
    elif spec["hair"] == "partline":
        hair = [(ox - HW * 1.02, oy + 0.25), (ox - HW * 0.95, oy + HH * 0.85), (ox - 0.2 + part, oy + HH * 1.12),
                (ox + 0.4 + part, oy + HH * 1.1), (ox + HW * 0.98, oy + HH * 0.8), (ox + HW * 1.02, oy + 0.3),
                (ox + HW * 0.75, oy + HH * 0.55), (ox + 0.1 + part, oy + HH * 0.72), (ox - 0.45 + part, oy + HH * 0.62),
                (ox - HW * 0.8, oy + HH * 0.45)]
    else:
        hair = [(ox - HW * 1.0, oy + 0.3), (ox - HW * 0.9, oy + HH * 0.95), (ox - 0.45 + part, oy + HH * 1.18),
                (ox - 0.15 + part, oy + HH * 1.05), (ox + 0.15 + part, oy + HH * 1.2), (ox + 0.45 + part, oy + HH * 1.07),
                (ox + HW * 0.9, oy + HH * 0.95), (ox + HW * 1.0, oy + 0.3), (ox + HW * 0.8, oy + HH * 0.62),
                (ox + part, oy + HH * 0.72), (ox - HW * 0.8, oy + HH * 0.62)]
    HC = spec.get("hair_color", "#1A1410")
    g.add(blob(hair, HC))
    if ay > 0.3 and spec["hair"] != "bun":   # back of the head shows more hair + a sideburn
        bxs = ox - sg * HW * 0.98
        g.add(blob([(bxs, oy + HH * 0.6), (bxs + sg * 0.32 * ay, oy + HH * 0.62), (bxs + sg * 0.22 * ay, oy + 0.05),
                    (bxs + sg * 0.05, oy - 0.1)], HC))

    # eyes
    wide, eo = P.get("wide", 0.0), P.get("eye_open", 1.0)
    look = P.get("look", (0.35 * yaw, 0.0))
    for side in (-1, 1):
        # the eye on the turning side is the far one: a bit narrower, tucked behind the nose
        far = 1 - 0.3 * max(0.0, side * yaw)
        ex = fx + side * (0.31 - 0.07 * max(0.0, side * yaw)) * (1 - 0.15 * ay)
        g.add(eye(ex, oy + 0.12, 0.3 * far, 0.34 * (0.92 + 0.08 * far), eo, look, wide, spec["skin"], P.get("lid", 0.1)))
    # brows
    b, wt = P.get("brow", 0.0), P.get("worry", 0.0)
    for side in (-1, 1):
        ex = fx + side * (0.31 - 0.07 * max(0.0, side * yaw)) * (1 - 0.15 * ay)
        by = oy + 0.5 + 0.14 * b + 0.16 * wide
        inner = (ex - side * 0.13, by - 0.01 + 0.09 * wt - 0.06 * P.get("frown", 0))
        outer = (ex + side * 0.15, by - 0.05 - 0.04 * wt)
        g.add(curve([inner, (ex + side * 0.01, by + 0.04), outer], sw=OL * 2.0))
    if spec.get("tilak"):
        g.add(Ellipse(width=0.07, height=0.13).move_to(_p(fx, oy + 0.55 + 0.1 * b)).set_fill("#C8102E", 1).set_stroke(width=0))
    if spec.get("bindi"):
        g.add(Circle(radius=0.055).move_to(_p(fx, oy + 0.42)).set_fill("#C8102E", 1).set_stroke(width=0))
    if spec.get("earrings"):
        for side in (-1, 1):
            if 1 - 2.2 * max(0.0, side * yaw) > 0.15:
                g.add(Circle(radius=0.07).move_to(_p(ox + side * HW * 0.97 + 0.12 * yaw, oy - 0.3)).set_fill("#F2C14E", 1).set_stroke(INK, 3))
    if spec.get("glasses"):
        for side in (-1, 1):
            ex = fx + side * (0.31 - 0.07 * max(0.0, side * yaw)) * (1 - 0.15 * ay)
            far = 1 - 0.3 * max(0.0, side * yaw)
            g.add(Ellipse(width=0.42 * far, height=0.36).move_to(_p(ex, oy + 0.12)).set_fill(opacity=0).set_stroke(INK, OL * 0.8))
        g.add(curve([(fx - 0.1, oy + 0.16), (fx, oy + 0.19), (fx + 0.1, oy + 0.16)], sw=OL * 0.8))
    # nose
    nx = fx + 0.12 * yaw
    if ay < 0.25:
        g.add(curve([(nx, oy + 0.02), (nx + 0.05, oy - 0.2), (nx - 0.08, oy - 0.26)], sw=OL))
    else:          # nose pokes out towards where he is looking
        g.add(blob([(nx - sg * 0.04, oy + 0.05), (nx + 0.2 * yaw, oy - 0.17), (nx + 0.12 * yaw, oy - 0.27), (nx - sg * 0.05, oy - 0.25)],
                   spec["shade"], sw=OL * 0.9))
    # moustache + mouth
    op, sm = P.get("mouth", 0.0), P.get("smile", 0.2)
    my = oy - 0.52
    if spec.get("moustache"):
        lift = 0.05 * op
        mx = fx + 0.12 * yaw
        must = [(mx - 0.38, oy - 0.42 + lift), (mx - 0.2, oy - 0.3 + lift), (mx, oy - 0.33 + lift), (mx + 0.2, oy - 0.3 + lift),
                (mx + 0.38, oy - 0.42 + lift), (mx + 0.2, oy - 0.43 + lift), (mx, oy - 0.4 + lift), (mx - 0.2, oy - 0.43 + lift)]
        g.add(mouth(mx, my - 0.02, 0.34, op, sm))
        g.add(blob(must, spec.get("hair_color", "#1A1410")))
    else:
        g.add(mouth(fx + 0.12 * yaw, my, 0.36 * (1 - 0.25 * ay), op, sm))
    return g


def head_back(spec, P, ox, oy):
    """Seen from behind: all hair, ears at the sides, a little neck skin."""
    HW, HH = 0.80, 0.95
    yaw = P.get("yaw", 0.0)                      # turning slightly shows a cheek edge
    HC = spec.get("hair_color", "#1A1410")
    g = VGroup()
    for side in (-1, 1):
        g.add(Ellipse(width=0.24, height=0.36).move_to(_p(ox + side * HW * 0.97, oy - 0.05)).set_fill(spec["skin"], 1).set_stroke(INK, OL))
    if abs(yaw) > 0.2:
        sg = 1 if yaw > 0 else -1
        g.add(blob([(ox + sg * HW * 0.9, oy + 0.1), (ox + sg * HW * 1.0, oy - 0.4), (ox + sg * HW * 0.6, oy - 0.85),
                    (ox + sg * HW * 0.5, oy - 0.2)], spec["skin"]))
    g.add(blob([(ox - HW, oy + 0.1), (ox - HW * 0.9, oy + HH * 0.8), (ox, oy + HH * 1.05), (ox + HW * 0.9, oy + HH * 0.8),
                (ox + HW, oy + 0.1), (ox + HW * 0.75, oy - HH * 0.55), (ox, oy - HH * 0.7), (ox - HW * 0.75, oy - HH * 0.55)], HC))
    if spec["hair"] == "bun":
        g.add(Circle(radius=0.34).move_to(_p(ox, oy + HH * 0.55)).set_fill(HC, 1).set_stroke(INK, OL))
        g.add(curve([(ox - 0.18, oy + HH * 0.55), (ox + 0.18, oy + HH * 0.62)], sw=OL * 0.6, color="#4A3A30"))
    return g


def puppy(t, x, y, s=1.0, pose=None, seed=7):
    """Tiny white puppy with a tied-up tuft of hair (ಜುಟ್ಟು). pose: yaw, mouth, tongue, wag, lick."""
    P = pose or {}
    g = VGroup()
    yaw = P.get("yaw", 0.0)
    wag = np.sin(t * 2 * np.pi * 4.5) * P.get("wag", 1.0)
    W, B = "#FBF7EE", "#C98A4B"
    # tail (behind body)
    g.add(limb((0.55, -0.35), (0.95 + 0.25 * wag, 0.05 + 0.1 * abs(wag)), 0.14, W))
    g.add(blob([(-0.6, -0.15), (0.0, 0.05), (0.62, -0.15), (0.68, -0.6), (0.3, -0.75), (-0.3, -0.75), (-0.66, -0.6)], W))   # body
    for dx in (-0.35, 0.35):
        g.add(blob([(dx - 0.13, -0.6), (dx + 0.13, -0.6), (dx + 0.14, -0.88), (dx - 0.14, -0.88)], W))                  # front paws
    hx, hy = 0.08 * yaw, 0.45
    for side in (-1, 1):                                                                                                   # floppy ears
        flop = 0.05 * np.sin(t * 9 + side)
        g.add(blob([(hx + side * 0.36, hy + 0.2), (hx + side * 0.62, hy + 0.05 + flop), (hx + side * 0.58, hy - 0.35 + flop),
                    (hx + side * 0.4, hy - 0.25)], B))
    g.add(Ellipse(width=0.92, height=0.82).move_to(_p(hx, hy)).set_fill(W, 1).set_stroke(INK, OL))                       # head
    g.add(Ellipse(width=0.3, height=0.26).move_to(_p(hx - 0.2 + 0.1 * yaw, hy + 0.12)).set_fill(B, 0.9).set_stroke(width=0))  # eye patch
    for side in (-1, 1):
        ex = hx + side * 0.17 + 0.08 * yaw
        g.add(Circle(radius=0.085).move_to(_p(ex, hy + 0.08)).set_fill("#1E1410", 1).set_stroke(width=0))
        g.add(Circle(radius=0.03).move_to(_p(ex + 0.03, hy + 0.11)).set_fill("#FFFFFF", 1).set_stroke(width=0))
    g.add(Ellipse(width=0.17, height=0.12).move_to(_p(hx + 0.1 * yaw, hy - 0.1)).set_fill("#1E1410", 1).set_stroke(width=0))  # nose
    if P.get("tongue", 0) > 0.2:
        g.add(blob([(hx - 0.07, hy - 0.2), (hx + 0.07, hy - 0.2), (hx + 0.06, hy - 0.2 - 0.22 * P["tongue"]), (hx - 0.06, hy - 0.2 - 0.22 * P["tongue"])],
                   "#E86A7A", sw=OL * 0.7))
    g.add(curve([(hx - 0.12, hy - 0.2), (hx, hy - 0.16), (hx + 0.12, hy - 0.2)], sw=OL * 0.8))
    # the tuft: a little fountain of hair on top, tied with a red ribbon
    bounce = 0.05 * np.sin(t * 7)
    for k in (-1, -0.35, 0.35, 1):     # a proud little fountain of hair
        tip = (hx + 0.22 * k, hy + 1.05 + bounce - 0.12 * abs(k))
        g.add(limb((hx + 0.03 * k, hy + 0.45), (hx + 0.07 * k, hy + 0.85 + bounce), 0.1, "#F3E7CF"))
        g.add(limb((hx + 0.07 * k, hy + 0.85 + bounce), tip, 0.08, "#F3E7CF"))
    g.add(blob([(hx - 0.22, hy + 0.6), (hx, hy + 0.5), (hx + 0.22, hy + 0.6), (hx + 0.22, hy + 0.4), (hx, hy + 0.48), (hx - 0.22, hy + 0.4)],
               "#E0323C", sw=OL * 0.8, smooth=False))                                                     # red ribbon bow
    g.add(Circle(radius=0.06).move_to(_p(hx, hy + 0.49)).set_fill("#E0323C", 1).set_stroke(INK, 4))
    g.scale(s, about_point=_p(0, 0)).shift(_p(x, y))
    return boil(g, t, seed)


# ---------------------------------------------------------------- body
def bag_shape(spec, bx, top):
    """Plastic shopping bag whose handles meet at (bx, top)."""
    g = VGroup()
    pts = [(-0.75, -0.3), (-0.35, 0.0), (0.35, 0.0), (0.75, -0.3), (0.82, -1.1), (0.4, -1.3), (-0.4, -1.3), (-0.82, -1.1)]
    g.add(blob([(bx + a, top + b) for a, b in pts], spec["bag"], opacity=0.92))
    g.add(curve([(bx - 0.32, top - 0.03), (bx - 0.2, top + 0.3), (bx - 0.08, top - 0.03)], sw=OL))
    g.add(curve([(bx + 0.08, top - 0.03), (bx + 0.2, top + 0.3), (bx + 0.32, top - 0.03)], sw=OL))
    if spec.get("bag_text"):
        tx = Text(spec["bag_text"], font="DejaVu Sans", weight="BOLD", color=INK).scale(0.16).move_to(_p(bx, top - 0.65))
        for m in [tx, *tx.family_members_with_points()]:
            m.no_boil = True
        g.add(tx)
    return g



def person_side(spec, P, t, x, y, s, seed):
    """Walking/standing in profile. P["side"] = +1 facing right, -1 facing left.
    P["phase"] = walk-cycle angle, P["walk"] = 0..1 how much they stride."""
    d = P.get("side", 1)
    ph, amp = P.get("phase", 0.0), P.get("walk", 1.0)
    g = VGroup()
    bob = 0.06 * amp * abs(np.sin(ph))
    oy = 0.02 * np.sin(t * 2 * np.pi / 3.6 + seed) + bob
    ox = 0.12 * d * amp                                  # a little forward lean while walking
    dark = lambda c: c                                    # far limbs: same colour, drawn behind

    def leg(phase_off, near):
        hip = np.array([0.15 * d * (1 if near else -1) * 0.3, -2.4 + oy])
        sw = np.sin(ph + phase_off) * amp
        foot = np.array([hip[0] + d * 0.85 * sw, -4.85 + 0.18 * max(0.0, np.cos(ph + phase_off)) * amp])
        knee = ik(hip, foot, 1.25, 1.25, bend=d)
        out = VGroup(limb(hip, knee, 0.52, spec["pants"]), limb(knee, foot, 0.46, spec["pants"]))
        out.add(Ellipse(width=0.7, height=0.26).move_to(_p(foot[0] + d * 0.18, foot[1] - 0.1)).set_fill("#2B1D14", 1).set_stroke(INK, OL))
        return out

    def arm(phase_off, near):
        sh = np.array([ox * 0.8, -0.35 + oy])
        a = 0.55 * np.sin(ph + phase_off) * amp
        hp = P.get("hand_near" if near else "hand_far")
        if hp is None:
            hp = sh + np.array([d * np.sin(a) * 2.0, -np.cos(a) * 2.0])
        el = ik(sh, hp, 1.15, 1.05, bend=-d)
        out = VGroup(limb(sh, el, 0.44, spec["shirt"]), limb(el, hp, 0.31, spec["skin"]))
        fore = np.array(hp) - el
        out.add(hand(hp, float(np.arctan2(fore[1], fore[0])), spec["skin"], spread=P.get("open_near" if near else "open_far", 0.2),
                     curl=0.3))
        return out

    g.add(leg(np.pi, False))
    g.add(arm(0.0, False))
    # torso in profile: chest bulges towards the facing side
    tor = [(ox - d * 0.55, oy + 0.05), (ox + d * 0.35, oy + 0.1), (ox + d * 0.75, oy - 0.5), (ox * 0.5 + d * 0.72, -2.45 + oy),
           (ox * 0.5 - d * 0.62, -2.45 + oy), (ox - d * 0.7, oy - 0.6)]
    g.add(blob([(-0.62, -2.25 + oy), (0.62, -2.25 + oy), (0.6, -2.85 + oy), (-0.6, -2.85 + oy)], spec["pants"]))
    g.add(leg(0.0, True))
    g.add(blob(tor, spec["shirt"]))
    g.add(blob([(ox - 0.2, oy + 0.35), (ox + 0.2, oy + 0.35), (ox + 0.2, oy - 0.08), (ox - 0.2, oy - 0.08)], spec["skin"]))
    HP = dict(P)
    HP["yaw"] = P.get("yaw", 1.0 * d)
    g.add(head(spec, HP, ox + d * 0.1 + 0.12 * P.get("tilt", 0.0), oy + 1.2))
    g.add(arm(np.pi, True))
    g.scale(s, about_point=_p(0, 0)).shift(_p(x, y))
    return boil(g, t, seed)


def person(spec, pose, t, x=0.0, y=0.0, s=1.0, seed=1):
    """Seated, seen from the front. (x, y) = base of the neck. Returns a boiled VGroup."""
    P = pose
    if P.get("side"):
        return person_side(spec, P, t, x, y, s, seed)
    lean, bob = P.get("lean", 0.0), P.get("bob", 0.0)
    breathe = 0.02 * np.sin(t * 2 * np.pi / 3.6 + seed)
    byaw = P.get("body_yaw", 0.35 * P.get("yaw", 0.0))
    g = VGroup()
    ox, oy = lean, bob + breathe                       # neck base in local units

    standing = P.get("standing", False)
    bag_at = P.get("bag_at", "lap")
    if standing:
        # legs: hips -> feet, straight with a little swing when walking
        sw_ = P.get("stride", 0.0)
        for side in (-1, 1):
            hip = (side * 0.5, -2.4)
            foot = (side * 0.55 + side * sw_ * 0.25, -4.85 + max(0.0, side * sw_) * 0.15)
            g.add(limb(hip, foot, 0.5, spec["pants"]))
            g.add(Ellipse(width=0.62, height=0.24).move_to(_p(foot[0] + side * 0.08, foot[1] - 0.12)).set_fill("#2B1D14", 1).set_stroke(INK, OL))
        g.add(blob([(-1.12, -2.3), (1.12, -2.3), (1.05, -2.95), (-1.05, -2.95)], spec["pants"]))
    else:
        # thighs (mostly below frame in a medium shot; the bag sits on them)
        g.add(blob([(-1.25, -2.45), (-0.1, -2.35), (0.1, -2.35), (1.25, -2.45), (1.35, -3.6), (-1.35, -3.6)], spec["pants"]))
    # torso: broad rounded shoulders tapering a little to the waist
    sh = 1.3
    tor = [(ox - sh, oy - 0.35), (ox - sh * 0.82, oy + 0.02), (ox - 0.3, oy + 0.1), (ox + 0.3, oy + 0.1),
           (ox + sh * 0.82, oy + 0.02), (ox + sh, oy - 0.35), (ox * 0.5 + 1.12, -2.5), (ox * 0.5 - 1.12, -2.5)]
    g.add(blob(tor, spec["shirt"]))
    cx = ox + 0.18 * byaw
    back = P.get("back", False)
    if spec.get("saree") and not back:
        g.add(blob([(ox - sh * 0.75, oy + 0.05), (ox - sh * 0.35, oy + 0.08), (ox * 0.5 + 1.05, -1.9), (ox * 0.5 + 1.12, -2.5),
                    (ox * 0.5 + 0.55, -2.5)], spec["saree"], smooth=False))
        g.add(curve([(ox - sh * 0.35, oy + 0.08), (ox * 0.5 + 1.05, -1.9)], sw=OL * 1.6, color=spec["saree_border"]))
    if back:
        pass
    elif spec["collar"] == "polo":
        g.add(blob([(cx - 0.45, oy + 0.02), (cx, oy - 0.45), (cx - 0.12, oy - 0.05)], spec["shirt_dark"], smooth=False))
        g.add(blob([(cx + 0.45, oy + 0.02), (cx, oy - 0.45), (cx + 0.12, oy - 0.05)], spec["shirt_dark"], smooth=False))
        g.add(curve([(cx, oy - 0.45), (cx, oy - 1.1)], sw=OL * 0.8))
        for k in range(2):
            g.add(Circle(radius=0.035).move_to(_p(cx + 0.07, oy - 0.62 - 0.22 * k)).set_fill(INK, 1).set_stroke(width=0))
    else:
        g.add(curve([(cx - 0.38, oy + 0.0), (cx, oy - 0.25), (cx + 0.38, oy + 0.0)], sw=OL))
    # neck (drawn over collar top, under head)
    g.add(blob([(ox - 0.22, oy + 0.35), (ox + 0.22, oy + 0.35), (ox + 0.2, oy - 0.08), (ox, oy - 0.2), (ox - 0.2, oy - 0.08)], spec["skin"]))

    # arms: shoulder -> hand (hands default resting on the bag, or hanging when standing)
    hands = []
    hpos_of = {}
    for side, key in ((-1, "hand_l"), (1, "hand_r")):
        shp = (ox + side * (sh - 0.22), oy - 0.3)
        default = (side * 1.45, -2.35) if standing else (side * 0.5, -2.05)
        hpos = P.get(key, default)
        hpos_of[key] = hpos
        elb = ik(shp, hpos, 1.15, 1.05, bend=-side if P.get(key + "_elbow_down") else side)
        g.add(limb(shp, elb, 0.46, spec["shirt"]))                 # short sleeve
        g.add(limb(elb, hpos, 0.32, spec["skin"]))
        fore = np.array(hpos) - elb
        d = P.get(key + "_dir", float(np.arctan2(fore[1], fore[0])))
        hands.append(hand(hpos, d, spec["skin"], spread=P.get(key + "_open", 0.2), curl=P.get(key + "_curl", 0.5)))

    # the shopping bag: on the lap, or hanging from a hand
    if bag_at and spec.get("bag"):
        if bag_at == "lap":
            bx, by = 0.0, -1.85
        else:
            hx, hy = hpos_of[bag_at]
            bx, by = hx, hy - 0.35
        g.add(bag_shape(spec, bx, by))
    for h in hands:
        g.add(h)

    if P.get("back", False):
        g.add(head_back(spec, P, ox + 0.12 * P.get("tilt", 0.0), oy + 1.2))
    else:
        g.add(head(spec, P, ox + 0.12 * P.get("tilt", 0.0), oy + 1.2))
    g.scale(s, about_point=_p(0, 0)).shift(_p(x, y))
    return boil(g, t, seed)
