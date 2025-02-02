from manim import *

class MyScene(Scene):
	def construct(self):
		num_plane = NumberPlane(background_line_style={"stroke_color": BLUE,
													   "stroke_opacity": 0.2})
		self.add(num_plane)
		txt = Text("Hello mr. Bond.").shift(UP * 2)
		self.play(Write(txt, rate_func=rate_functions.ease_in_sine))
		self.wait(2)
		self.play(Unwrite(txt))

		sqr = Rectangle(fill_color=PINK, fill_opacity=0.4)
		self.add(sqr)
		tor = Torus(color=PINK, major_radius=2, minor_radius=0.5)
		self.play(Write(sqr))
		self.wait(2)
		self.play(Transform(sqr, tor))
		self.wait(3)
		self.play(Rotate(tor, -120*DEGREES, about_point=ORIGIN))
		self.wait(2)
