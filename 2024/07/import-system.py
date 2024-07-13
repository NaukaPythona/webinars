#!./present Intro Modularity Strategies

from __future__ import annotations

from manim import *
from manim_slides import Slide
from slothy import lazy_importing

with lazy_importing():
    import os
    import sys

    import theme


class Intro(Slide):
    def construct(self) -> None:
        title = theme.title(
            "Jak działają importy w Pythonie?",
            place=UP,
            color=theme.BRIGHT_PYTHON_BLUE,
        )
        underline = theme.underline(title)
        self.play(theme.title_anim(title, underline))

        self.next_slide()

        logotype = theme.logotype()
        logotype.next_to(underline, direction=DOWN * 2)
        self.play(FadeIn(logotype))

        self.next_slide()


class Modularity(Slide):
    def construct(self) -> None:
        self.play(theme.title_anim("1. Problem modularności"))
        self.next_slide()


class Strategies(Slide):
    def construct(self) -> None:
        self.play(theme.title_anim("2. Importery"))
        self.next_slide()


if __name__ == "__main__":
    os.execlp(__file__, *sys.argv)
