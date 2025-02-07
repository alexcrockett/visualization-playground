from manim import *

class RotatingObjects(Scene):
    def construct(self):
        circ_a = Circle(color=PINK)
        circ_b = Circle(color=BLUE_C)
        self.play(Create(circ_a), Create(circ_b))
        self.wait(2)
        self.play(circ_a.animate.move_arc_center_to(RIGHT), 
                  circ_b.animate.move_arc_center_to(LEFT))
        self.wait(2)
        shapes = VGroup(circ_a, circ_b)
        self.play(Rotate(shapes, angle=PI))
        self.wait(2)



