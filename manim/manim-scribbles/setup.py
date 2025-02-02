from manim import *

class hello(Scene):
	def construct(self):
		t = Tex ("hello world")
		self. play(Write(t))
		self.wait (3)