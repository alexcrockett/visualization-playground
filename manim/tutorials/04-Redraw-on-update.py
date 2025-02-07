from manim import *

class RedrawOnUpdate(Scene):
    def construct(self):

        # Draw two circles to connect with a line
        circ1 = Circle(color=PINK)
        circ2 = Circle(color=BLUE_C)

        # Draw and reposition the circles
        self.play(Create(circ1))
        self.wait(1)
        self.play(circ1.animate(rate_functions=double_smooth).move_to(LEFT*2))
        self.wait(1)
        self.play(Create(circ2))
        self.wait(2)
        self.play(circ2.animate(rate_functions=double_smooth).move_to(RIGHT*2))
        self.wait(2)

        # Draw a line connecting the two circles
        connect = always_redraw(lambda:Line(buff=0.5, start=circ1.get_right(), end=circ2.get_left(), color=GREEN_D))
        self.play(Create(connect))
        self.wait(2)

        # Now we move the circles, the line's distance will be updated
        self.play(circ1.animate(rate_functions=double_smooth).move_to([-3, 0, 0]))
        self.play(circ2.animate(rate_functions=double_smooth).move_to([3, 0, 0]))
        self.wait(3)



