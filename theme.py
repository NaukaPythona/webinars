from __future__ import annotations

import manim
from slothy import type_importing

with type_importing():
    from pathlib import Path
    from typing import Final

    import numpy as np


FONT: Final = "Liberation Mono"
LOGO_PATH: Path = Path("assets/logotype.png")

DARK_PYTHON_BLUE: Final = manim.ManimColor("#306998")
DARKER_PYTHON_BLUE: Final = manim.ManimColor("#306998", alpha=0.5)
BRIGHT_PYTHON_BLUE: Final = manim.ManimColor("#65A4D2")
PYTHON_BLUE: Final = BRIGHT_PYTHON_BLUE
PYTHON_YELLOW: Final = manim.ManimColor("#ffe262")


def underline(
    mobject: manim.Mobject,
    color: manim.ManimColor | None = None,
) -> manim.Line:
    underline = manim.Line(color=color or DARKER_PYTHON_BLUE)
    underline.stretch_to_fit_width(mobject.width)
    underline.next_to(mobject, direction=manim.DOWN)
    return underline


def underline_anim(
    mobject: manim.Mobject,
    underline: manim.Line,
) -> manim.LaggedStart:
    return manim.LaggedStart(
        manim.GrowFromCenter(mobject),
        manim.GrowFromCenter(underline),
    )


def title(
    content: str,
    place: np.ndarray = manim.UP * 3,
    color: manim.ManimColor | None = None,
) -> manim.Text:
    title = manim.Text(
        content,
        font=FONT,
        color=color or DARK_PYTHON_BLUE,
    )
    title.move_to(place)
    return title


def title_anim(
    title_text_or_mobject: manim.Text | str,
    underline_mobject: manim.Line | None = None,
) -> manim.LaggedStart:
    if isinstance(title_text_or_mobject, str):
        title_mobject = title(title_text_or_mobject)
    else:
        title_mobject = title_text_or_mobject
    if underline_mobject is None:
        underline_mobject = underline(title_mobject)
    return underline_anim(title_mobject, underline_mobject)


def logotype(scale: float = 0.6) -> manim.ImageMobject:
    image = manim.ImageMobject(LOGO_PATH)
    image.scale(scale)
    return image
