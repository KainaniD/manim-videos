from manimlib import *
import numpy as np
import random as rand

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

def createNode(data):
    data = str(data)
    node = VGroup()
    node_data = Text(data)
    node_circle = Circle(radius=0.7, stroke_color=RED)
    node_circle.set_fill(RED, opacity=0.2)
    node.add(node_data, node_circle)
    return node

def createData(data):
    data = str(data)
    node = VGroup()
    node_data = Text(data)
    node_data.scale(0.8)
    node_square = Square(side_length=1, stroke_color=WHITE)
    node_square.set_fill(WHITE, opacity=0)
    node.add(node_data, node_square)
    return node

def createDataFixedWidth(data, width):
    data = str(data)
    node = VGroup()
    node_data = Text(data)
    node_data.scale(0.8)
    node_rectangle = Rectangle(width=width, height=1, stroke_color=WHITE)
    node_rectangle.set_fill(WHITE, opacity=0)
    node.add(node_data, node_rectangle)
    return node

def swap(first, second):
    first.generate_target()
    second.generate_target()
    first.target.shift(second.get_center()- first.get_center())
    second.target.shift(first.get_center() - second.get_center())

def play_swap(self, first, second, third, fourth):
    self.play(MoveToTarget(first), MoveToTarget(second), MoveToTarget(third), MoveToTarget(fourth), run_time=1)

class Array(Scene):
    def construct(self):
        intro_words = Text("""
            What is an Array?
        """).to_edge(UP).scale(1.2)

        array_group = VGroup()
        array_data_values = []

        for i in range(9):
            num = rand.randint(0, 99)
            data = createData(num).shift(LEFT * 4 + RIGHT * i + DOWN)
            array_group.add(data)
            array_data_values.append(num)
        
        self.play(Write(intro_words), FadeIn(array_group), run_time=1)

        index_label_group_array = []
        center_text_array = []

        for i in range(9):
            index_label_group = VGroup()
            index_label = Text(f"""array[{i}]""", t2c={f"[{i}]": BLUE}).shift(LEFT * 4 + RIGHT * i + UP).scale(0.8)
            index_label_arrow = Line(index_label, array_group[i]).scale(0.8).add_tip()
            index_label_highlight = Square(side_length=1, color=BLUE).shift(LEFT * 4 + RIGHT * i + DOWN)

            index_label_group.add(index_label).add(index_label_arrow).add(index_label_highlight)

            index_label_group_array.append(index_label_group)

            center_text_array.append(Text(f"""array[{i}]=={array_data_values[i]}""", t2c={f"[{i}]": BLUE, f"{array_data_values[i]}": RED}).shift(UP * 2).scale(0.8))
    

        self.play(Write(index_label_group_array[0]))

        index_text_group = VGroup()

        index_text = Text("""index""", t2c={"index": BLUE}).shift(LEFT + UP).scale(0.8)
        index_text_line = Line(index_text, index_label_group_array[0][0]).scale(0.8).add_tip()

        index_text_group.add(index_text).add(index_text_line)

        self.play(FadeIn(index_text_group))
        self.wait(0.5)
        self.play(FadeOut(index_text_group))

        self.play(Write(center_text_array[0]), FadeToColor(array_group[0][0], RED))

        for i in range(1, 9):
            self.wait(1)
            self.play(Transform(index_label_group_array[0], index_label_group_array[i]), Transform(center_text_array[0], center_text_array[i]), FadeToColor(array_group[i-1][0], WHITE), FadeToColor(array_group[i][0], RED))
        self.wait(2)