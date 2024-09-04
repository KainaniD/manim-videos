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


class Pointers(Scene):
    def construct(self):
        
        
        intro_words = Text("""
            What is a pointer?
        """)
        intro_words.to_edge(UP)
        intro_words.scale(1.2)

        myNum_label = Text("""
        myNum
        """)
        myNum_label.shift(UP)
        myNum_label.scale(0.9)

        myNum_node = createNode("""5""")
        
        variable_name_label = Text("""
        variable name
        """)
        variable_name_label.shift(UP + LEFT*3)
        variable_name_label.scale(0.8)

        variable_data_label = Text("""
        variable data
        """)
        variable_data_label.shift(LEFT*3)
        variable_data_label.scale(0.8)

        self.play(Write(intro_words), Write(myNum_label), Write(myNum_node[0]), ShowCreation(myNum_node[1]), run_time = 1)
        
        self.play(Write(variable_data_label), Write(variable_name_label), run_time = 0.5)
        self.wait(2)
        self.play(FadeOut(variable_data_label), FadeOut(variable_name_label), run_time = 0.5)
        
        pointer_label = Text("""
        myNumPointer
        """)
        pointer_label.shift(LEFT*2 + UP*2)
        pointer_label.scale(0.9)

        pointer_data = createData("""0x6dfed4""")
        pointer_data.shift(LEFT*2 + UP)

        myNum_group = VGroup()
        myNum_group.add(myNum_node, myNum_label)
        myNum_group.generate_target()
        myNum_group.target.shift(RIGHT*2 + UP)
        self.play(MoveToTarget(myNum_group), run_time = 1)
        pointer_data_to_myNum = Line(start=pointer_data, end=myNum_node)
        pointer_data_to_myNum.add_tip()
        self.play(Write(pointer_label), Write(pointer_data[0]), ShowCreation(pointer_data[1]), Write(pointer_data_to_myNum), run_time = 1)
        


        myChar_label = Text("""
        myChar
        """)
        myChar_label.shift(RIGHT*2 + DOWN)
        myChar_label.scale(0.9)

        myChar_node = createNode("""c""")
        myChar_node.shift(RIGHT*2 + DOWN*2)
        self.play(Write(myChar_label), Write(myChar_node[0]), ShowCreation(myChar_node[1]), run_time = 1)

        pointer_label2 = Text("""
        myCharPointer
        """)
        pointer_label2.shift(LEFT*2 + DOWN)
        pointer_label2.scale(0.9)

        pointer_data2 = createData("""0x68b3a2""")
        pointer_data2.shift(LEFT*2 + DOWN*2)

        pointer_data2_to_myNum2 = Line(start=pointer_data2, end=myChar_node)
        pointer_data2_to_myNum2.add_tip()

        self.play(Write(pointer_label2), Write(pointer_data2[0]), Write(pointer_data2_to_myNum2), ShowCreation(pointer_data2[1]), run_time = 1)
        self.wait(6)