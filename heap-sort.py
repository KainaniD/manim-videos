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
    node_rectangle.set_fill(BLACK, opacity=0.3)
    node.add(node_data, node_rectangle)
    return node

def swap(first, second):
    first.generate_target()
    second.generate_target()
    first.target.shift(second.get_center()- first.get_center())
    second.target.shift(first.get_center() - second.get_center())

def playSwap(self, element1, element2):
    self.play(MoveToTarget(element1), MoveToTarget(element2), run_time=1)

def playDoubleSwap(self, element1, element2, element3, element4):
    self.play(MoveToTarget(element1), MoveToTarget(element2), MoveToTarget(element3), MoveToTarget(element4), run_time=1)

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

def createArray(element):
    return VGroup().add(element)

def addToArray(array, element):
    array.add(element.shift(array[-1].get_center() + DOWN))

def createStack(element):
    return VGroup().add(element)

def addToStack(self, stack, new_element):
    new_element.shift(stack[-1].get_center() + UP)
    self.play(FadeInFromPoint(new_element, stack[-1].get_center() + UP * 2))
    stack.add(new_element)

def removeFromStack(self, stack):
    self.play(FadeOutToPoint(stack[-1], stack[-1].get_center() + UP))
    stack.remove(stack[-1])

def createQueue(element):
    return VGroup().add(element)

def addToQueue(self, queue, new_element):
    new_element.shift(queue[-1].get_center())
    queue.generate_target()
    queue.target.shift(UP)
    self.play(FadeInFromPoint(new_element, queue[-1].get_center() + DOWN), MoveToTarget(queue))
    queue.add(new_element)

def removeFromQueue(self, queue):
    self.play(FadeOutToPoint(queue[0], queue[0].get_center() + UP))
    queue.remove(queue[0])    

def updateText(self, text, new_text, scale = 0.8):
    transformedText = Text(new_text).shift(text.get_center()).scale(scale)
    self.play(Transform(text, transformedText), run_time = 0.75)
    self.wait(0.5)

class HeapSort(Scene):
    def construct(self):
        intro_words = Text("""
            What is Heap Sort?
        """).to_edge(UP).scale(1.2)

        buffer_1 = 0.35
        buffer_2 = 0.31
        heap_tree = createGraph(createNode(9)).shift(UP * 2 + LEFT * 2)
        addNodeToGraph(heap_tree, heap_tree[0], createNode(8), -2, 1, buffer_1)
        addNodeToGraph(heap_tree, heap_tree[0], createNode(5), 2, 1, buffer_1)
        addNodeToGraph(heap_tree, heap_tree[1], createNode(4), -1, 2, buffer_2)
        addNodeToGraph(heap_tree, heap_tree[1], createNode(1), 1, 2, buffer_2)
        addNodeToGraph(heap_tree, heap_tree[3], createNode(3), -1, 2, buffer_2)
        addNodeToGraph(heap_tree, heap_tree[3], createNode(2), 1, 2, buffer_2)

        9, 8, 5, 4, 3, 2, 1

        heap = createArray(createRectangleNode(9, 3, 1)).shift(RIGHT * 4 + UP * 2.5)
        addToArray(heap, createRectangleNode(8, 3, 1))
        addToArray(heap, createRectangleNode(5, 3, 1))
        addToArray(heap, createRectangleNode(4, 3, 1))
        addToArray(heap, createRectangleNode(1, 3, 1))
        addToArray(heap, createRectangleNode(3, 3, 1))
        addToArray(heap, createRectangleNode(2, 3, 1))
        heap.scale(0.8)

        current_action = Text("""
            current step
        """).shift(LEFT * 2 + DOWN * 2.5).scale(0.8)

        self.play(Write(intro_words), Write(heap_tree), Write(heap), Write(current_action))
        self.wait(1)

        updateText(self, current_action, """swap first and last node""")
        swap(heap_tree[0], heap_tree[-2])
        swap(heap[0], heap[-1])
        playDoubleSwap(self, heap[0], heap[-1], heap_tree[0], heap_tree[-2])

        updateText(self, current_action, """remove last node from tree""")
        self.play(FadeOut(heap_tree[0]), FadeOut(heap_tree[12]), FadeToColor(heap[0][1], GREEN))

        updateText(self, current_action, """heapify""")
        swap(heap_tree[11], heap_tree[1])
        swap(heap[-1], heap[1])
        playDoubleSwap(self, heap_tree[1], heap_tree[11], heap[-1], heap[1])
        swap(heap_tree[11], heap_tree[5])
        swap(heap[-1], heap[3])
        playDoubleSwap(self, heap_tree[5], heap_tree[11], heap[-1], heap[3])

        updateText(self, current_action, """swap first and last node""")
        swap(heap_tree[9], heap_tree[1])
        swap(heap[-2], heap[1])
        playDoubleSwap(self, heap_tree[1], heap_tree[9], heap[-2], heap[1])

        updateText(self, current_action, """remove last node from tree""")
        self.play(FadeOut(heap_tree[1]), FadeOut(heap_tree[10]), FadeToColor(heap[1][1], GREEN))

        updateText(self, current_action, """heapify""")
        swap(heap_tree[9], heap_tree[3])
        swap(heap[-2], heap[2])
        playDoubleSwap(self, heap_tree[9], heap_tree[3], heap[-2], heap[2])

        updateText(self, current_action, """swap first and last node""")
        swap(heap_tree[3], heap_tree[7])
        swap(heap[-3], heap[2])
        playDoubleSwap(self, heap_tree[3], heap_tree[7], heap[-3], heap[2])

        updateText(self, current_action, """remove last node from tree""")
        self.play(FadeOut(heap_tree[3]), FadeOut(heap_tree[8]), FadeToColor(heap[2][1], GREEN))

        updateText(self, current_action, """heapify""")
        swap(heap_tree[7], heap_tree[5])
        swap(heap[-3], heap[3])
        playDoubleSwap(self, heap_tree[7], heap_tree[5], heap[-3], heap[3])
        swap(heap_tree[7], heap_tree[11])
        swap(heap[4], heap[6])
        playDoubleSwap(self, heap_tree[7], heap_tree[11], heap[4], heap[6])

        updateText(self, current_action, """swap first and last node""")
        swap(heap_tree[5], heap_tree[7])
        swap(heap[-3], heap[3])
        playDoubleSwap(self, heap_tree[5], heap_tree[7], heap[-3], heap[3])
    
        updateText(self, current_action, """remove last node from tree""")
        self.play(FadeOut(heap_tree[5]), FadeOut(heap_tree[6]), FadeToColor(heap[3][1], GREEN))

        updateText(self, current_action, """heapify""")
        swap(heap_tree[7], heap_tree[9])
        swap(heap[4], heap[5])
        playDoubleSwap(self, heap_tree[7], heap_tree[9], heap[4], heap[5])

        updateText(self, current_action, """swap first and last node""")
        swap(heap_tree[7], heap_tree[9])
        swap(heap[4], heap[5])
        playDoubleSwap(self, heap_tree[7], heap_tree[9], heap[4], heap[5])

        updateText(self, current_action, """remove last node from tree""")
        self.play(FadeOut(heap_tree[9]), FadeOut(heap_tree[4]), FadeToColor(heap[5][1], GREEN))

        updateText(self, current_action, """heapify""")
        swap(heap_tree[7], heap_tree[11])
        swap(heap[6], heap[4])
        playDoubleSwap(self, heap_tree[7], heap_tree[11], heap[4], heap[6])

        updateText(self, current_action, """swap first and last node""")
        swap(heap_tree[7], heap_tree[11])
        swap(heap[6], heap[4])
        playDoubleSwap(self, heap_tree[7], heap_tree[11], heap[4], heap[6])

        updateText(self, current_action, """remove last node from tree""")
        self.play(FadeOut(heap_tree[2]), FadeOut(heap_tree[11]), FadeToColor(heap[6][1], GREEN))

        updateText(self, current_action, """heapify""")
        updateText(self, current_action, """swap first and last node""")
        updateText(self, current_action, """remove last node from tree""")
        self.play(FadeOut(heap_tree[7]), FadeToColor(heap[4][1], GREEN))

        heap.generate_target()
        heap.target.shift(LEFT * 4)
        self.play(FadeOut(current_action), MoveToTarget(heap))
        self.wait(1)