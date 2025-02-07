from manim import *

class Ellipse(Scene):
    def construct(self):
        ellipse_1 = Ellipse()
        self.add(ellipse_1)
        self.play(Create(ellipse_1))
        self.wait(2)

