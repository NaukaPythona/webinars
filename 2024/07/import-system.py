#!./present -S Intro

from manim import *
from manim_slides import Slide
from slothy import lazy_importing

with lazy_importing():
    import os
    import sys

    import theme


class Intro(Slide):
    def construct(self) -> None:
        text = Text(
            "Jak działają importy w Pythonie?",
            font=theme.FONT,
            color=theme.BRIGHT_PYTHON_BLUE,
        )

        underline = Line(color=theme.DARKER_PYTHON_BLUE)
        underline.stretch_to_fit_width(text.width)
        underline.next_to(text, direction=DOWN)

        self.play(
            GrowFromCenter(text),
            GrowFromCenter(underline),
        )

        self.next_slide()



if __name__ == "__main__":
    os.execlp(__file__, *sys.argv)
