from manimlib import *
import numpy as np

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
    node_square = Square(side_length=2, stroke_color=WHITE)
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

class MinHeap(Scene):
    def construct(self):
        intro_words = Text("""
            What is a min-heap?
        """)
        intro_words.to_edge(UP)
        intro_words.scale(1.2)

        tree1 = createNode(12)
        tree1.shift(LEFT * 2 + UP * 2)
        array1 = createDataFixedWidth(12, 3)
        array1.shift(RIGHT * 5 + UP * 2)

        self.play(Write(intro_words), run_time=1)
        self.play(Write(tree1), Write(array1), run_time=1)
        self.wait(0.4)
        self.play(FadeToColor(tree1[1], BLUE))

        tree2 = createNode(8)
        tree2.shift(LEFT * 4)
        tree1_tree2 = Line(start=tree1, end=tree2)
        tree1_tree2.scale(1.7)
        array2 = createDataFixedWidth(8, 3)
        array2.shift(RIGHT * 5 + UP)
        self.play(Write(tree2), Write(array2), Write(tree1_tree2), run_time=1)
        self.wait(0.4)

        swap(tree1, tree2)
        swap(array1, array2)
        play_swap(self, tree1, array1, tree2, array2)
        self.wait(0.4)
        self.play(FadeToColor(tree2[1], BLUE))

        tree3 = createNode(10)
        tree2_tree3 = Line(start=tree2, end=tree3)
        tree2_tree3.scale(1.7)
        array3 = createDataFixedWidth(10, 3)
        array3.shift(RIGHT * 5)
        self.play(Write(tree3), Write(array3), Write(tree2_tree3), run_time=1)
        self.wait(0.4)
        self.play(FadeToColor(tree3[1], BLUE))

        tree4 = createNode(6)
        tree4.shift(LEFT * 5 + DOWN * 2)
        tree1_tree4 = Line(start=tree1, end=tree4)
        tree1_tree4.scale(1.2)
        array4 = createDataFixedWidth(6, 3)
        array4.shift(RIGHT * 5 + DOWN)

        self.play(Write(tree4), Write(array4), Write(tree1_tree4), run_time=1)
        self.wait(0.4)

        swap(tree4, tree1)
        swap(array4, array1)
        play_swap(self, tree1, array1, tree4, array4)

        swap(tree4, tree2)
        swap(array4, array2)
        play_swap(self, tree2, array2, tree4, array4)
        self.wait(0.4)
        self.play(FadeToColor(tree4[1], BLUE))

        tree5 = createNode(7)
        tree5.shift(LEFT * 3 + DOWN * 2)
        tree2_tree5 = Line(start = tree2, end = tree5)
        tree2_tree5.scale(1.2)
        array5 = createDataFixedWidth(7, 3)
        array5.shift(RIGHT * 5 + DOWN * 2)
        self.play(Write(tree5), Write(array5), Write(tree2_tree5), run_time=1)
        self.wait(0.4)

        swap(tree5, tree2)
        swap(array5, array2)
        play_swap(self, tree2, array2, tree5, array5)
        self.wait(0.4)
        self.play(FadeToColor(tree5[1], BLUE))

        tree6 = createNode(2)
        tree6.shift(LEFT + DOWN * 2)
        tree3_tree6 = Line(start=tree3, end=tree6)
        tree3_tree6.scale(1.2)
        array6 = createDataFixedWidth(2, 3)
        array6.shift(RIGHT * 5 + DOWN * 3)
        self.play(Write(tree6), Write(array6), Write(tree3_tree6), run_time=1)
        self.wait(0.4)

        swap(tree3, tree6)
        swap(array3, array6)
        play_swap(self, tree3, array3, tree6, array6)

        swap(tree4, tree6)
        swap(array4, array6)
        play_swap(self, tree4, array4, tree6, array6)
        self.wait(0.4)
        self.play(FadeToColor(tree6[1], BLUE))
