from manim import * 


class BinaryMultiplication(Scene):
    def construct(self):
        multiplicand = Text('1010', color=BLUE)
        multiplier = Text('1101', color=ORANGE).next_to(multiplicand, DOWN)
        self.play(Write(multiplicand))
        self.wait(1)
        self.play(Write(multiplier))
        
        # moving multiplicand to top left
        self.play(multiplicand.animate.shift(2.5*UP).shift(4*LEFT).scale(0.6))
        # moving multiplier to top right
        self.play(multiplier.animate.next_to(multiplicand, RIGHT).scale(0.6))
        self.play(multiplier.animate.shift(6*RIGHT)) 
        # Multiplicand Text
        cand_text = Text('Multiplicand', color=BLUE, font_size=24).next_to(multiplicand, UP)
        # Multiplier Text
        plier_text = Text('Multiplier', color=ORANGE, font_size=24).next_to(multiplier, UP)

        self.play(Write(cand_text))
        self.play(Write(plier_text))
        self.wait(1)

        # expand multiplicand bits 
        exp_multiplicand = Text('0000', color=BLUE).next_to(multiplicand, LEFT).scale(0.6)
        self.play(Write(exp_multiplicand))
        self.play(multiplicand.animate.shift(0.5*LEFT))  # cand closer to exp
        multiplicand_whole = VGroup(multiplicand, exp_multiplicand)  # group the two objects
        
        # expand multiplier bits 
        exp_multiplier = Text('0000', color=ORANGE).next_to(multiplier, LEFT).scale(0.6)
        self.play(Write(exp_multiplier))
        self.play(multiplier.animate.shift(0.5*LEFT))  # cand closer to exp
        multiplier_whole = VGroup(multiplier, exp_multiplier)  # group the two objects

        self.play(multiplicand_whole.animate.shift(RIGHT), multiplier_whole.animate.shift(RIGHT))

        
        self.wait(1) 
