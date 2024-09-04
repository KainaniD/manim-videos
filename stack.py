from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.



def createNode(data):
    node = VGroup()
    node_data = Text(data)
    node_circle = Circle(stroke_color=BLUE)
    node_circle.set_fill(BLUE, opacity=0.5)
    node_circle.surround(node_data, buff=0.5)
    node.add(node_data, node_circle)
    return node

def createData(data):
    node = VGroup()
    node_data = Text(data)
    node_data.scale(0.8)
    node_square = Square(stroke_color=WHITE)
    node_square.set_fill(WHITE, opacity=0)
    node_square.surround(node_data, buff=0.5)
    node.add(node_data, node_square)
    return node

def createDataFixedWidth(data):
    node = VGroup()
    node_data = Text(data)
    node_data.scale(0.8)
    node_rectangle = Rectangle(width=4, height=1, stroke_color=WHITE)
    node_rectangle.set_fill(WHITE, opacity=0)
    node.add(node_data, node_rectangle)
    return node

class Stack(Scene):
    def construct(self):
        
        
        intro_words = Text("""
            What is a stack?
        """)
        intro_words.to_edge(UP)
        intro_words.scale(1.2)

        first = createDataFixedWidth("""20""")
        first.shift(DOWN*2)
        second = createDataFixedWidth("""29""")
        second.shift(DOWN)
        third = createDataFixedWidth("""10""")
        fourth = createDataFixedWidth("""35""")
        fourth.shift(UP)

        stack_group_add = VGroup()
        stack_group_add.add(first, second, third, fourth)

        stack_group_subtract = VGroup()
        stack_group_subtract.add(fourth, third)

        accessing_label = Text("""
            accessing
        """)
        accessing_label.scale(0.9)
        accessing_label.shift(LEFT*4 + DOWN*2)
        accessing_label_to_first = Line(start=accessing_label, end=first)
        accessing_label_to_first.add_tip()
        accessing_label_to_first.scale(0.7)
        accessing = VGroup()
        accessing.add(accessing_label, accessing_label_to_first)

        self.play(Write(intro_words), FadeInFromPoint(first, first.get_top() + UP), run_time=1)
        self.play(Write(accessing), run_time=1)

        for i in range(1, len(stack_group_add)):
            accessing.generate_target()
            accessing.target.shift(UP)
            self.play(FadeInFromPoint(stack_group_add[i], stack_group_add[i].get_top() + UP), MoveToTarget(accessing), run_time=1)
            self.wait(0.2)
        self.wait(1)
        for i in range(len(stack_group_subtract)):
            accessing.generate_target()
            accessing.target.shift(DOWN)
            self.play(FadeOutToPoint(stack_group_subtract[i], stack_group_subtract[i].get_top() + UP), MoveToTarget(accessing), run_time=1)
            self.wait(0.2)
        self.wait(8)
        


