from manim import * 


class VectorArrow(Scene):  # inherit from Scene 
    def construct(self):
        dot = Dot(ORIGIN)  # create a point at (0, 0)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        number_plane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT) 
        self.add(number_plane, dot, arrow, origin_text, tip_text)  # to the scene


