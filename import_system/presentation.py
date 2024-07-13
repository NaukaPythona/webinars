#!./present Intro Modularity Strategies Outro

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
            gradient=(theme.BRIGHT_PYTHON_BLUE, theme.PYTHON_YELLOW),
        )
        underline = theme.underline(title)
        self.play(theme.title_anim(title, underline))
        self.next_slide()

        logotype = theme.logotype()
        logotype.next_to(underline, direction=DOWN * 2)
        self.play(FadeIn(logotype))
        self.next_slide()


WITHOUT_IMPORT = """\
class Point2D:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
"""


WITH_IMPORT = """\
from typing import NamedTuple


class Point2D(NamedTuple):
    x: int
    y: int
"""


ONLY_IMPORT = """\
from typing import NamedTuple
"""


CODE_OPTIONS = {
    "tab_width": 4,
    "language": "Python",
    "background_stroke_color": DARK_BLUE,
}


class Modularity(Slide):
    def construct(self) -> None:
        title = theme.title("1. Problem modularności")
        underline = theme.underline(title)
        self.play(theme.title_anim(title, underline))
        self.next_slide()

        bullet_points = [
            "→ Cel: umożliwienie wykorzystywania\n  kodu w zewnętrznych miejscach",
            "→ Pojawia się niemal w każdym języku",
            "→ Jest często kluczowy, by budować\n  podstawowe rozwiązania",
        ]
        text = MarkupText("...", font=theme.FONT)
        self.next_slide()
        for i in range(1, len(bullet_points) + 1):
            text_string = "\n".join(bullet_points[:i])
            new_text = MarkupText(
                text_string,
                justify=True,
                font=theme.FONT,
                font_size=28,
                tab_width=2,
                width=10,
            )
            self.play(text.animate.become(new_text))
            self.next_slide()

        self.remove(text)
        self.play(title.animate.become(theme.title("1. Problem modularności (Python)")))
        self.play(underline.animate.stretch_to_fit_width(title.width))
        self.next_slide()

        code = Code(code=WITHOUT_IMPORT, **CODE_OPTIONS)
        self.play(FadeIn(code))
        self.next_slide()

        self.play(code.animate.become(Code(code=WITH_IMPORT, **CODE_OPTIONS)))
        self.next_slide()


class Strategies(Slide):
    def construct(self) -> None:
        code = Code(code=WITH_IMPORT, **CODE_OPTIONS)
        self.play(theme.title_anim("2. Importery"), FadeIn(code))
        self.next_slide()

        self.play(code.animate.become(Code(code=ONLY_IMPORT, **CODE_OPTIONS)))
        self.next_slide()

        new_options = {
            **CODE_OPTIONS,
            "insert_line_no": False,
        }

        self.play(
            code.animate.become(
                Code(code=ONLY_IMPORT, **new_options).align_on_border(LEFT)
            )
        )
        self.next_slide()

        finders = [
            "built-in importer",
            "frozen importer",
            "file finder",
        ]

        finder_mobjects = [
            Code(code=finder_repr.join("<>"), **new_options) for finder_repr in finders
        ]

        metapath = Group(
            Code(
                code="sys.meta_path",
                **{**new_options, "background_stroke_width": 3},
            ),
            Group(*finder_mobjects).arrange(DOWN),
        )
        metapath.arrange(DOWN)
        metapath.next_to(code)

        self.play(Indicate(code), FadeIn(metapath))
        self.wait()
        self.next_slide()

        for i, finder_mobject in enumerate(finder_mobjects, start=1):
            self.play(Wiggle(finder_mobject))
            self.wait()
            if i != len(finder_mobjects):
                self.play(
                    ShowPassingFlashWithThinningStrokeWidth(
                        finder_mobject, remover=False
                    )
                )
                self.play(finder_mobject.animate.scale(0.4))
            else:
                self.play(Flash(finder_mobject))

                found = Code(
                    code="/foo/bar/lib/python3.11/typing.py",
                    background_stroke_width=3,
                    **new_options,
                )
                found.next_to(finder_mobject, direction=DOWN)
                self.play(ReplacementTransform(finder_mobject, found))


class Outro(Slide):
    def construct(self) -> None:
        title = theme.title(
            "EOF",
            place=UP,
            gradient=(theme.PYTHON_YELLOW, theme.BRIGHT_PYTHON_BLUE),
        )
        underline = theme.underline(title)
        self.play(theme.title_anim(title, underline))
        logotype = theme.logotype()
        logotype.next_to(underline, direction=DOWN * 2)
        self.play(FadeIn(logotype))
        self.next_slide()
        self.play(*map(FadeOut, (title, underline, logotype)))


if __name__ == "__main__":
    os.execlp(__file__, *sys.argv)  # Requires chmod +x on __file__
