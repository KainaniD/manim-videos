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

def createDataFixedWidth(data, width):
    node = VGroup()
    node_data = Text(data)
    node_data.scale(0.8)
    node_rectangle = Rectangle(width=width, height=1, stroke_color=WHITE)
    node_rectangle.set_fill(WHITE, opacity=0)
    node.add(node_data, node_rectangle)
    return node


class Hashmap(Scene):
    def construct(self):
        intro_words = Text("""
            What is a hashmap?
        """)
        intro_words.to_edge(UP)
        intro_words.scale(1.2)

        function_divider = Line(LEFT * 2 + UP * 2, LEFT * 2 + DOWN * 3)

        key_group = VGroup()
        bucket_group = VGroup()
        value_group = VGroup()

        key_group.add(createDataFixedWidth("""Student1""", 3).shift(LEFT*4 + UP*(1/2)), createDataFixedWidth("""Student2""", 3).shift(LEFT*4 + DOWN*(3/2)))
        
        for i in range(4):
            bucket_group.add(createDataFixedWidth(str(i), 1).shift(UP + DOWN*i))
        
        value_group.add(createDataFixedWidth("""""", 4).shift(RIGHT*3 + UP), createDataFixedWidth("""""", 4).shift(RIGHT*3), createDataFixedWidth("""""", 4).shift(RIGHT*3 + DOWN), createDataFixedWidth("""""", 4).shift(RIGHT*3 + DOWN*2))

        self.play(Write(intro_words), Write(key_group), Write(bucket_group), Write(value_group), Write(function_divider), run_time=1)

        self.wait(1)

        self.play(Write(Line(key_group[0], LEFT * 2 + UP*(1/2))))
        self.play(Write(Line(LEFT * 2 + UP*(1/2), LEFT*(1/2) + DOWN)))
        self.play(Write(Line(RIGHT*(1/2) + DOWN, value_group[2])))

        transform_value_one = createDataFixedWidth("""A-""", 4).shift(RIGHT*3 + DOWN)
        self.play(ReplacementTransform(value_group[2], transform_value_one))

        self.wait(1)

        self.play(Write(Line(key_group[1], LEFT * 2 + DOWN*(3/2))))
        self.play(Write(Line(LEFT * 2 + DOWN*(3/2), LEFT*(1/2) + UP)))
        self.play(Write(Line(RIGHT*(1/2) + UP, value_group[0])))

        transform_value_two = createDataFixedWidth("""B+""", 4).shift(RIGHT*3 + UP)
        self.play(ReplacementTransform(value_group[0], transform_value_two))
        self.wait(16)