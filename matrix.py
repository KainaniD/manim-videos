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

class Matrix(Scene):
    def construct(self):
        intro_words = Text("""
            What is a matrix?
        """)
        intro_words.to_edge(UP)
        intro_words.scale(1.2)

        matrix = []
        matrixGroup = VGroup()

        for i in range(20):
            currentData = createData(rand.randint(0, 99))
            matrixGroup.add(currentData)
            matrix.append(currentData)

        index = 0
        for i in range(4):
            for j in range(5):
                matrix[index].shift(DOWN * i * 1.2 + RIGHT * j)
                index+=1

        matrixGroup.shift(LEFT * 2 + UP * 2)

        side_key = VGroup()
        bottom_key = VGroup()
        array_key = VGroup()

        for i in range(4):
            side_key.add(Text(f'{i}').shift(LEFT * 3.5 + UP * 2 + DOWN * i * 1.2))

        for i in range(5):
            bottom_key.add(Text(f'{i}').shift(LEFT * 2 + RIGHT * i + DOWN * 3))

        for i in range(4):
            array_key.add(Text(f'Array {i + 1}').shift(RIGHT * 4.5 + UP * 2 + DOWN * i * 1.2))

        self.play(Write(intro_words), run_time = 1)
        self.play(FadeIn(matrixGroup), run_time = 1)
        self.play(FadeIn(array_key), run_time = 1)
        self.wait(0.5)
        self.play(Write(side_key), Write(bottom_key), run_time = 1)

        self.wait(0.5)
        self.play(FadeOut(array_key), run_time = 1)

        index_text = Text("Accessing:\n\nmatrix[3]", t2c={"[3]": RED})
        index_text.shift(RIGHT * 4.5 + UP)
        index_text.scale(0.8)
        self.play(Write(index_text), FadeToColor(matrixGroup[15:20], RED), FadeToColor(matrixGroup[0:15], GREY), FadeToColor(side_key[3], RED), FadeToColor(side_key[0:3], GREY),run_time = 1)
        self.wait(2)
        index_text1 = Text("Accessing:\n\nmatrix[3][2]", t2c={"[3]": RED, "[2]": BLUE})
        index_text1.shift(RIGHT * 4.5 + UP)
        index_text1.scale(0.8)
        self.play(ReplacementTransform(index_text, index_text1), FadeToColor(matrixGroup[17], BLUE), FadeToColor(bottom_key, GREY), FadeToColor(bottom_key[2], BLUE), run_time = 1)
        self.wait(2)
        self.play(FadeOut(index_text1), FadeToColor(matrixGroup, WHITE), FadeToColor(bottom_key, WHITE), FadeToColor(side_key, WHITE), run_time=1)
        self.wait(1)
        index_text2 = Text("Accessing:\n\nmatrix[0]", t2c={"[0]": RED})
        index_text2.shift(RIGHT * 4.5 + UP)
        index_text2.scale(0.8)
        self.play(FadeToColor(matrixGroup, GREY), FadeToColor(side_key, GREY), Write(index_text2), FadeToColor(matrixGroup[0:5], RED), FadeToColor(side_key[0], RED), run_time = 1)
        self.wait(2)
        index_text3 = Text("Accessing:\n\nmatrix[0][1]", t2c={"[0]": RED, "[1]": BLUE})
        index_text3.shift(RIGHT * 4.5 + UP)
        index_text3.scale(0.8)
        self.play(ReplacementTransform(index_text2, index_text3), FadeToColor(matrixGroup[1], BLUE), FadeToColor(bottom_key, GREY), FadeToColor(bottom_key[1], BLUE), run_time = 1)
        self.wait(2)