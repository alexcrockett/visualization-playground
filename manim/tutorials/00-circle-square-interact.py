from manim import *

class CircleSquareInteract(Scene):
    def construct(self):

        # Here we create the circle and square
        circle = Circle(radius=0.5, stroke_width=5, color="#FFFF2A", fill_color="#FFFF2A", fill_opacity=0.5)
        square = Square(side_length=1.2, stroke_width=10, color="#833AFF")
        rect = SurroundingRectangle(square, color=BLUE_A, stroke_width=15, corner_radius=0.3)
        grid = NumberPlane(x_range=[-7, 7, 1], y_range=[-4, 4, 1], axis_config={"color": BLUE_B})

        # Here we animate the circle and square
        self.play(DrawBorderThenFill(circle), Create(square))
        self.wait(2)

        # Here we animate the rectangle and the circle and square
        self.play(Create(rect))
        self.play(circle.animate.move_to([-2, 0, 0]))
        self.play(square.animate.move_to([2, 0, 0]))
        self.play(Create(grid))

        # Wait 3 seconds before looping
        self.wait(3)
