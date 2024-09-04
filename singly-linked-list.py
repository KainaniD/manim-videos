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



class LinkedList(Scene):
    def construct(self):
        
        
        intro_words = Text("""
            What is a linked list?
        """)
        intro_words.to_edge(UP)
        intro_words.scale(1.2)

        head_label = Text("""
        head
        """)
        head_label.shift(LEFT*4 + UP)
        head_label.scale(0.9)

        current_label = Text("""
                             current
                             """)
        current_label.shift(LEFT*3 + DOWN*1)
        current_label.scale(0.9)

        head_node = createNode(2)
        head_node.scale(2)
        head_node.shift(UP)

        self.play(Write(intro_words), Write(head_label), Write(head_node[0]), ShowCreation(head_node[1]), run_time = 1)
        head_label_to_head_node0 = Line(start=head_label, end=head_node, buff=0.2)
        self.play(ShowCreation(head_label_to_head_node0), run_time = 0.5)
        self.wait(1)
        

        head_label.generate_target()
        head_label.target.shift(UP)
        head_node.generate_target()
        head_node.target.shift(LEFT*3 + DOWN*1)
        head_node.target.scale(1/2)
        head_label_to_head_node1 = Line(start=head_label.target, end=head_node.target, buff=0.2)
        self.play(MoveToTarget(head_node), MoveToTarget(head_label), ReplacementTransform(head_label_to_head_node0, head_label_to_head_node1), run_time = 0.5)

        
        child1_node = createNode(3)
        head_node_to_child1_node = Line(start=head_node, end=child1_node, buff=0)
        head_node_to_child1_node.add_tip()
        self.play(Write(head_node_to_child1_node), run_time = 0.5)
        self.play(Write(child1_node[0]), ShowCreation(child1_node[1]), run_time = 0.5)


        child2_node = createNode(9)
        child2_node.shift(RIGHT*3)
        child1_node_to_child2_node = Line(start=child1_node, end=child2_node, buff=0)
        child1_node_to_child2_node.add_tip()
        self.play(Write(child1_node_to_child2_node), run_time = 0.5)
        self.play(Write(child2_node[0]), ShowCreation(child2_node[1]), run_time = 0.5)


        self.wait(0.5)
        self.play(Write(current_label), FadeToColor(head_node[1], color=RED), run_time = 0.4)
        current_label.generate_target()
        current_label.target.shift(RIGHT*3)
        self.wait(0.5)
        self.play(MoveToTarget(current_label), FadeToColor(head_node[1], color=BLUE), FadeToColor(child1_node[1], color=RED), run_time = 0.4)
        current_label.generate_target()
        current_label.target.shift(RIGHT*3)
        self.wait(0.5)
        self.play(MoveToTarget(current_label), FadeToColor(child1_node[1], color=BLUE), FadeToColor(child2_node[1], color=RED), run_time = 0.4)
        self.wait(6)
        
