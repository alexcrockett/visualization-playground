from manim import *

class CircleSquareArrow(Scene):
    def construct(self):

        # Here we create the circle, square and triangle
        circle = Circle(radius=0.5, stroke_width=5, color="#FFFF2A", fill_color="#FFFF2A", fill_opacity=0.5)
        square = Square(side_length=1.2, stroke_width=5, color="#833AFF")
        triangle = Triangle(color=RED_D, stroke_width=5)

        # Here we create the circle and square      
        self.play(DrawBorderThenFill(circle), Create(square))
        self.wait(2)

        # Here we create the triangle
        self.play(Write(triangle))
        self.wait(2)

        # Here we move the circle, square and triangle to their respective positions
        self.play(circle.animate.move_to([-3, -2, 0]))
        self.play(square.animate.move_to([0, 2, 0]))
        self.play(triangle.animate.move_to([3, -2, 0]))
        self.wait(2)
        
        # Here we create the arrows
        arrow_1 = Line(start=circle.get_top(), end=square.get_bottom(), color=GREEN_D, stroke_width=5, buff=0.3).add_tip()
        arrow_2 = Line(start=square.get_bottom(), end=triangle.get_top(), color=BLUE_D, stroke_width=5, buff=0.3).add_tip()
        arrow_3 = Line(start=triangle.get_top(), end=circle.get_top(), color=RED_D, stroke_width=5, buff=0.3).add_tip()

        # Here we create the arrows
        self.play(Create(arrow_1))
        self.wait(2)
        self.play(Create(arrow_2))
        self.wait(2)
        self.play(Create(arrow_3))
        self.wait(2)
