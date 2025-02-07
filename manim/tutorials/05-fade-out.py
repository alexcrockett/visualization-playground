from manim import *

class FadeOutObjects(Scene):
    def construct(self):
        # Create three circles
        circle1 = Circle(color=PINK, fill_opacity=0.5)
        circle2 = Circle(color=BLUE, fill_opacity=0.5)
        circle3 = Circle(color=GREEN, fill_opacity=0.5)
        
        # Draw the circles
        self.play(DrawBorderThenFill(circle1), DrawBorderThenFill(circle2), DrawBorderThenFill(circle3))

        # Move the circles
        self.play(circle1.animate(rate_functions=double_smooth).move_to([-1, 0, 0]))
        self.play(circle2.animate(rate_functions=double_smooth).move_to([0, 0, 0]))
        self.play(circle3.animate(rate_functions=double_smooth).move_to([1, 0, 0]))

        # Fade out the circles in a circular manner
        self.play(FadeOut(circle1))
        self.play(FadeOut(circle2))
        self.play(DrawBorderThenFill(circle1), FadeOut(circle3))
        self.play(DrawBorderThenFill(circle2), FadeOut(circle1))
        self.play(DrawBorderThenFill(circle3), FadeOut(circle2))
        self.play(DrawBorderThenFill(circle1), FadeOut(circle3))
        self.play(DrawBorderThenFill(circle2), FadeOut(circle1), FadeOut(circle2))
        self.play(DrawBorderThenFill(circle3))
        self.play(ShrinkToCenter(circle3))