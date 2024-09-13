from manimlib import *
import numpy as np
import random as rand

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

def createNode(data, radius=0.5):
    data = str(data)
    node = VGroup()
    node_data = Text(data)
    node_circle = Circle(radius=radius, stroke_color=WHITE)
    #node_circle.set_fill(BLUE, opacity=0.2)
    node.add(node_data, node_circle)
    return node

def createRectangleNode(data, width=1, height=1):
    data = str(data)
    node = VGroup()
    node_data = Text(data)
    node_data.scale(0.8)
    node_rectangle = Rectangle(width=width, height=height, stroke_color=WHITE)
    node_rectangle.set_fill(WHITE, opacity=0)
    node.add(node_data, node_rectangle)
    return node

def swap(first, second):
    first.generate_target()
    second.generate_target()
    first.target.shift(second.get_center()- first.get_center())
    second.target.shift(first.get_center() - second.get_center())
    return VGroup().add(first, second)

def playSwap(self, group):
    self.play(MoveToTarget(group), run_time=1)

def highlight(self, color, item, color2=WHITE, *items):
    item_group = VGroup()
    for i in items:
        item_group.add(i)
    self.play(FadeToColor(item, color), FadeToColor(item_group, color2), run_time=0.75)

def createGraph(node):
    return VGroup().add(node)

def addNodeToGraph(graph, graph_node, new_node, x_offset, y_offset, buffer):
    new_node = new_node.shift(graph_node.get_center() + RIGHT * x_offset + DOWN * y_offset)
    graph.add(new_node).add(Line(start=graph_node[0], end=new_node[0], buff=buffer).add_tip())

def createStack(element):
    return VGroup().add(element)

def addToStack(self, stack, new_element):
    new_element.shift(stack[-1].get_center() + UP)
    self.play(FadeInFromPoint(new_element, stack[-1].get_center() + UP * 2))
    stack.add(new_element)

def removeFromStack(self, stack):
    self.play(FadeOutToPoint(stack[-1], stack[-1].get_center() + UP))
    stack.remove(stack[-1])

class DepthSearch(Scene):
    def construct(self):
        intro_words = Text("""
            What is Depth First Search?
        """)
        intro_words.to_edge(UP)
        intro_words.scale(1.2)


        buffer_1 = 0.35
        buffer_2 = 0.31
        tree = createGraph(createNode("""a""")).shift(UP * 2 + LEFT * 2)
        addNodeToGraph(tree, tree[0], createNode("""b"""), -2, 1, buffer_1)
        addNodeToGraph(tree, tree[0], createNode("""c"""), 2, 1, buffer_1)
        addNodeToGraph(tree, tree[1], createNode("""d"""), -1, 2, buffer_2)
        addNodeToGraph(tree, tree[1], createNode("""e"""), 1, 2, buffer_2)
        addNodeToGraph(tree, tree[3], createNode("""f"""), -1, 2, buffer_2)
        addNodeToGraph(tree, tree[3], createNode("""g"""), 1, 2, buffer_2)
        addNodeToGraph(tree, tree[5], createNode("""h"""), -1, 2, buffer_2)
        addNodeToGraph(tree, tree[7], createNode("""i"""), -1, 2, buffer_2)
        addNodeToGraph(tree, tree[7], createNode("""j"""), 1, 2, buffer_2)
        addNodeToGraph(tree, tree[11], createNode("""k"""), 1, 2, buffer_2)

        stack = createStack(createRectangleNode("""a""", 3, 1)).shift(RIGHT * 5 + DOWN * 3)

        self.play(Write(intro_words), Write(tree))

        highlight(self, RED, tree[0])
        self.play(FadeInFromPoint(stack, stack[0].get_center() + UP))

        highlight(self, RED, tree[2], GREY, tree[0])

        highlight(self, RED, tree[1], GREY, tree[2])
        addToStack(self, stack, createRectangleNode("""b""", 3, 1))
        highlight(self, RED, tree[6], GREY, tree[1])

        highlight(self, RED, tree[5], GREY, tree[6])
        addToStack(self, stack, createRectangleNode("""d""", 3, 1))
        highlight(self, RED, tree[14], GREY, tree[5])

        highlight(self, RED, tree[13], GREY, tree[14])
        addToStack(self, stack, createRectangleNode("""h""", 3, 1))
        self.wait(0.5)
        removeFromStack(self, stack)

        highlight(self, RED, tree[5], GREY, tree[13])
        removeFromStack(self, stack)
        highlight(self, RED, tree[1], GREY, tree[5])

        highlight(self, RED, tree[8], GREY, tree[1])

        highlight(self, RED, tree[7], GREY, tree[8])
        addToStack(self, stack, createRectangleNode("""e""", 3, 1))
        highlight(self, RED, tree[16], GREY, tree[7])

        highlight(self, RED, tree[15], GREY, tree[16])
        addToStack(self, stack, createRectangleNode("""i""", 3, 1))
        self.wait(0.5)
        removeFromStack(self, stack)
        highlight(self, RED, tree[7], GREY, tree[15])
        highlight(self, RED, tree[18], GREY, tree[7])

        highlight(self, RED, tree[17], GREY, tree[18])
        addToStack(self, stack, createRectangleNode("""j""", 3, 1))
        self.wait(0.5)
        removeFromStack(self, stack)
        highlight(self, RED, tree[7], GREY, tree[17])
        removeFromStack(self, stack)
        highlight(self, RED, tree[1], GREY, tree[7])
        removeFromStack(self, stack)
        highlight(self, RED, tree[0], GREY, tree[1])
        

        highlight(self, RED, tree[4], GREY, tree[0])
        highlight(self, RED, tree[3], GREY, tree[4])
        addToStack(self, stack, createRectangleNode("""c""", 3, 1))
        highlight(self, RED, tree[10], GREY, tree[3])

        highlight(self, RED, tree[9], GREY, tree[10])
        addToStack(self, stack, createRectangleNode("""f""", 3, 1))
        self.wait(0.5)
        removeFromStack(self, stack)
        highlight(self, RED, tree[3], GREY, tree[9])
        highlight(self, RED, tree[12], GREY, tree[3])

        highlight(self, RED, tree[11], GREY, tree[12])
        addToStack(self, stack, createRectangleNode("""g""", 3, 1))
        highlight(self, RED, tree[20], GREY, tree[11])

        highlight(self, RED, tree[19], GREY, tree[20])
        addToStack(self, stack, createRectangleNode("""k""", 3, 1))
        self.wait(0.5)
        removeFromStack(self, stack)

        highlight(self, RED, tree[11], GREY, tree[19])
        removeFromStack(self, stack)
        highlight(self, RED, tree[3], GREY, tree[11])
        removeFromStack(self, stack)
        highlight(self, RED, tree[0], GREY, tree[3])
        removeFromStack(self, stack)
        highlight(self, GREY, tree[0])
        self.wait(1)