from manim import * 


class BinaryMultiplication(Scene):
    def construct(self):
        cand_bits = [Integer(number=1, color=BLUE), Integer(number=0, color=BLUE), Integer(number=1, color=BLUE), Integer(number=0, color=BLUE)]
        plier_bits = [Integer(number=1, color=ORANGE), Integer(number=1, color=ORANGE), Integer(number=0, color=ORANGE), Integer(number=1, color=ORANGE)]
        
        multiplicand = VGroup(cand_bits[0], cand_bits[1], cand_bits[2], cand_bits[3])        
        multiplier = VGroup(plier_bits[0], plier_bits[1], plier_bits[2], plier_bits[3])

        cand_bits[0].shift(LEFT)
        plier_bits[0].shift(RIGHT)

        for i in range(1, 4):
            cand_bits[i].next_to(cand_bits[i-1], RIGHT)
            plier_bits[i].next_to(plier_bits[i-1], RIGHT) 
        
        self.play(Write(multiplicand))
        self.play(multiplicand.animate.shift(2*LEFT))
        self.wait(1)
        self.play(Write(multiplier))
        
        # moving multiplicand to top left
        self.play(multiplicand.animate.shift(2.5*UP).shift(1*LEFT).scale(0.6))
        # moving multiplier to top right
        self.play(multiplier.animate.shift(2.5*UP).shift(2*RIGHT).scale(0.6)) 
        # Multiplicand Text
        cand_text = Text('Multiplicand', color=BLUE, font_size=24).next_to(multiplicand, UP)
        # Multiplier Text
        plier_text = Text('Multiplier', color=ORANGE, font_size=24).next_to(multiplier, UP)

        self.play(Write(cand_text))
        self.play(Write(plier_text))
        self.wait(1)

        # Product
        product_rect = Rectangle(width=8.0, height=1.0, grid_xstep=1.0)
        product_text = Text('Product (8-bits)', color=PURPLE, font_size=24).next_to(product_rect, DOWN)
        self.play(Write(product_rect), Write(product_text))

        # Move Multiplier bits into Product Rectangle 
        self.play(multiplier[3].animate.shift(2.5*DOWN, 0.75*LEFT).scale(1.3))
        self.play(multiplier[2].animate.shift(2.5*DOWN, 1.45*LEFT).scale(1.3))
        self.play(multiplier[1].animate.shift(2.5*DOWN, 2.10*LEFT).scale(1.3))
        self.play(multiplier[0].animate.shift(2.5*DOWN, 2.80*LEFT).scale(1.3))

        # Move the 'Multiplier' text down 
        self.play(plier_text.animate.shift(2.25*DOWN, 1.75*LEFT))

        # displaying product bits 
        product_bits = [Integer(number=0, color=ORANGE), Integer(number=0, color=ORANGE), Integer(number=0, color=ORANGE), Integer(number=0, color=ORANGE)]
        self.play(Write(product_first_4))

        self.play(multiplicand.animate.shift(1.65*DOWN, 1.5*RIGHT).scale(1.3))
        self.play(multiplicand[0].animate.shift(1.2*LEFT), multiplicand[1].animate.shift(0.6*LEFT), 
                multiplicand[2].animate.shift(0.05*LEFT), multiplicand[3].animate.shift(0.55*RIGHT),
                cand_text.animate.shift(1.3*DOWN, 1.2*RIGHT))

        addition_sign = Text("+", color=YELLOW, font_size=30).next_to(product_rect, LEFT)

        for iteration in range(4):
            # if there is a 1, we add product (first 4) with multiplier (4 bits) AND THEN shift WHOLE Product to the right by 1 bit
            # step 1: Add animation of multiplicand plus product's first four bits 
            if multiplier[-1].text == "1":
                # Frame the LSB of Product (Multiplier0)
                frame_last_bit = SurroundingRectangle(multiplier[3], buff=.1, color=YELLOW)
                self.play(Write(frame_last_bit))
                self.play(Write(addition_sign))

                # step 2: Show the addition's answer 
                cand_bin = multiplicand[0] + multiplicand[1] + multiplicand[2] + multiplicand[3]
                prod_bin = "".join([p.text for p in product_first_4[:4]])
                addition_result = list((bin(int(cand_bin,2) + int(prod_bin,2)))[2:])

                # step 3: Change the first four bits of the product 
                for i in range(4):
                    product_first_4[i].text = addition_result[i] 

                self.play(FadeOut(product_first_4))
                
                self.play(Write(product_first_4))
                self.play(FadeOut(frame_last_bit), FadeOut(multiplier[-1]), FadeOut(addition_sign))
                # actually take out last multiplier bit since it's no longer needed
                multiplier.remove(multiplier[-1])

            # step 4: Shift the ENTIRE product grid by 1 bit to the right 
            # add 0 bit to the left 
            product_first_4.insert(0, Text('0', color=PURPLE).next_to(product_first_4[0], 2.85*LEFT).scale(0.78))
            prod_mul_group = VGroup(product_first_4, multiplier)
            self.play(prod_mul_group.animate.shift(RIGHT))
