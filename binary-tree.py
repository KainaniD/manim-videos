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
    node_data = Integer(data)
    node_circle = Circle(stroke_color=BLUE)
    node_circle.set_fill(BLUE, opacity=0.5)
    node_circle.surround(node_data, buff=0.5)
    node.add(node_data, node_circle)
    return node



class BinaryTree(Scene):
    def construct(self):
        
        
        intro_words = Text("""
            What is a binary tree?
        """)
        intro_words.to_edge(UP)
        intro_words.scale(1.2)

        root_label = Text("""
        root
        """)
        root_label.shift(LEFT*4 + UP)
        root_label.scale(0.9)

        root_node = createNode(5)
        root_node.scale(2)
        root_node.shift(UP)

        self.play(Write(intro_words), Write(root_label), Write(root_node[0]), ShowCreation(root_node[1]), run_time = 1)
        root_label_to_root_node0 = Line(start=root_label, end=root_node, buff=0.2)
        self.play(ShowCreation(root_label_to_root_node0), run_time = 0.5)
        self.wait(1)

        root_label.generate_target()
        root_label.target.shift(RIGHT*2 + UP)
        root_node.generate_target()
        root_node.target.shift(UP)
        root_node.target.scale(1/2)
        root_label_to_root_node1 = Line(start=root_label.target, end=root_node.target, buff=0.2)
        self.play(MoveToTarget(root_node), MoveToTarget(root_label), ReplacementTransform(root_label_to_root_node0, root_label_to_root_node1), run_time = 0.5)


        left_node = createNode(3)
        left_node.shift(LEFT*2)
        right_node = createNode(8)
        right_node.shift(RIGHT*2)
        root_node_to_left_node = Line(start=root_node[0], end=left_node[0], buff=0.5)
        root_node_to_left_node.add_tip()
        root_node_to_right_node = Line(start=root_node[0], end=right_node[0], buff=0.5)
        root_node_to_right_node.add_tip()

        self.play(Write(right_node[0]), ShowCreation(right_node[1]), Write(left_node[0]), ShowCreation(left_node[1]), run_time = 0.5)
        self.play(Write(root_node_to_left_node), Write(root_node_to_right_node), run_time = 0.5)
        
        left_left_node = createNode(1)
        left_left_node.shift(LEFT*3 + DOWN*2)
        left_right_node = createNode(4)
        left_right_node.shift(LEFT + DOWN*2)
        right_right_node = createNode(9)
        right_right_node.shift(RIGHT*3 + DOWN*2)

        left_node_to_left_left_node = Line(start=left_node, end=left_left_node)
        left_node_to_left_left_node.add_tip()
        left_node_to_left_right_node = Line(start=left_node, end=left_right_node)
        left_node_to_left_right_node.add_tip()
        right_node_to_right_right_node = Line(start=right_node, end=right_right_node)
        right_node_to_right_right_node.add_tip()

        self.play(Write(left_left_node[0]), ShowCreation(left_left_node[1]), Write(left_right_node[0]), ShowCreation(left_right_node[1]), Write(right_right_node[0]), ShowCreation(right_right_node[1]), run_time = 0.5)
        self.play(Write(left_node_to_left_left_node), Write(left_node_to_left_right_node), Write(right_node_to_right_right_node), run_time = 0.5)
        
        self.wait(3)
        self.wait(0.5)
        self.play(FadeToColor(root_node[1], color=RED), run_time = 0.4)
        self.wait(0.5)
        self.play(FadeToColor(root_node[1], color=BLUE), FadeToColor(left_node[1], color=RED), run_time = 0.4)
        self.wait(0.5)
        self.play(FadeToColor(left_node[1], color=BLUE), FadeToColor(left_right_node[1], color=RED), run_time = 0.4)
        self.wait(6)
        
