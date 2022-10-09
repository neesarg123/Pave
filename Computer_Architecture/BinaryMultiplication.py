from manim import *


class BinaryMultiplication(Scene):
    def construct(self):
        # multiplicand (sample: 1010)
        cand_bits = [Integer(number=1, color=BLUE), Integer(number=0, color=BLUE), Integer(number=1, color=BLUE), Integer(number=0, color=BLUE)]
        # multiplier (sample: 1101)
        plier_bits = [Integer(number=1, color=ORANGE), Integer(number=1, color=ORANGE), Integer(number=0, color=ORANGE), Integer(number=1, color=ORANGE)]

        # adding the multiplicand and multiplier into the scene
        # step 1: Group together multiplicand bits 
        multiplicand = VGroup(cand_bits[0], cand_bits[1], cand_bits[2], cand_bits[3])
        # step 2: Group together multiplier bits 
        multiplier = VGroup(plier_bits[0], plier_bits[1], plier_bits[2], plier_bits[3])
        # step 3: move the LSB of multiplicand left a little
        multiplicand[0].shift(LEFT)
        # step 4: repeat step 3 but for multiplier and move it right a little 
        multiplier[0].shift(RIGHT)
        # step 5: separate every bit in the multiplicand and multiplier from one another
        for i in range(1, 4):
            multiplicand[i].next_to(multiplicand[i-1], RIGHT)
            multiplier[i].next_to(multiplier[i-1], RIGHT)
        # step 6: add all elements to the scene 
        self.add(multiplicand, multiplier)
        # step 7: write all the elements onto the screen
        self.play(Write(multiplicand), Write(multiplier))
        self.wait(1)
        
        # move the multiplicand to upper left corner
        self.play(multiplicand.animate.shift(2.5*UP, LEFT))
        # move the multiplier to the upper right corner 
        self.play(multiplier.animate.shift(2.5*UP, RIGHT))

        # adding "Multiplicand" text
        cand_text = Text("Multiplicand", color=BLUE, font_size=24).next_to(multiplicand, UP)
        # adding "Multiplier" text 
        plier_text = Text("Multiplier", color=ORANGE, font_size=24).next_to(multiplier, UP)
        # adding objects to the scene
        self.add(cand_text, plier_text) 
        # animating screen
        self.play(Write(cand_text), Write(plier_text)) 
        self.wait(1) 

        # adding Product grid and text
        product_rect = Rectangle(width=8, height=1, grid_xstep=1)
        # text 
        product_text = Text("Product (8-bits)", color=PURPLE, font_size=24).next_to(product_rect, DOWN)
        # adding both to the scene 
        self.add(product_text, product_rect)
        # animating screen 
        self.play(Write(product_rect), Write(product_text))
        self.wait(1)

        # moving Multiplier bits into the Product
        self.play(multiplier[3].animate.shift(2.5*DOWN, 0.2*RIGHT))
        self.play(multiplier[2].animate.shift(2.5*DOWN, 0.35*LEFT))
        self.play(multiplier[1].animate.shift(2.5*DOWN, 0.9*LEFT))
        self.play(multiplier[0].animate.shift(2.5*DOWN, 1.5*LEFT))

        # moving the Multiplier text down
        self.play(plier_text.animate.shift(2.25*DOWN, 0.9*LEFT))

        # Showing the first four product bits (initially 0 0 0 0)
        product_initial = [Integer(number=0, color=PURPLE), Integer(number=0, color=PURPLE), Integer(number=0, color=PURPLE), Integer(number=0, color=PURPLE)]
        product = VGroup(product_initial[0], product_initial[1], product_initial[2], product_initial[3])
        product[0].shift(3.5*LEFT)
        for i in range(1, 4):
            product[i].next_to(product[i-1], 3.15*RIGHT)
        self.play(Write(product))
        
        # Moving the Multiplicand bits down
        self.play(multiplicand.animate.shift(1.5*DOWN), cand_text.animate.shift(1.5*DOWN))
        self.play(multiplicand[0].animate.shift(1.5*LEFT), multiplicand[1].animate.shift(0.95*LEFT), multiplicand[2].animate.shift(0.4*LEFT),
                  multiplicand[3].animate.shift(0.2*RIGHT))
        
        # Initializing an Addition Sign
        addition_sign = Text("+", color=YELLOW, font_size=30).next_to(product_rect, LEFT)

        # Main Loop
        for i in range(4):
            next_bit = 0
            # if the LSB of Multiplier is 1, then we add Multiplicand with first 4 bits of Product
            if multiplier[-1].get_value() == 1:
                # Draw a YELLOW frame around the bit
                frame_last_bit = SurroundingRectangle(multiplier[-1], buff=0.1, color=YELLOW)
                self.play(Write(frame_last_bit))
                # Draw the Addition Sign
                self.play(Write(addition_sign))

                # Perform the addition
                cand_binary = "".join(str(c.get_value()) for c in multiplicand)
                product_binary = "".join(str(p.get_value()) for p in product[:4])
                addition_result = list((bin(int(cand_binary, 2) + int(product_binary, 2)))[2:])
                if len(addition_result) > 4:
                    next_bit = 1

                # Overwrite first four bits of Product with the addition_result
                if len(addition_result) == 4:
                    for i in range(4):
                        product[i].set_value(int(addition_result[i]))
                else:
                    for i in range(4):
                        product[i].set_value(int(addition_result[i+1]))

                self.play(Write(product))

                self.play(FadeOut(addition_sign))

            # Remove Addition Sign and the LSB of Multiplier
            self.play(FadeOut(multiplier[-1]), FadeOut(frame_last_bit))
            # Removing the LSB of Multiplier from its VGroup as it is no longer needed
            multiplier.remove(multiplier[-1])

            # Shift the Product bits (including the Multiplier bits) to the right once
            product.insert(0, Integer(next_bit, color=PURPLE).next_to(product[0], 3.2*LEFT))
            self.play(FadeIn(product[0]))

            # Making a new VGroup of Product and Multiplier to move them together
            product_multiplier_group = VGroup(product, multiplier)
            # Drawing animation of Product and Multiplier moving to the right
            self.play(product_multiplier_group.animate.shift(RIGHT))
                
