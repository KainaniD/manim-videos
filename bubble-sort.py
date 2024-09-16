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
    node_rectangle.set_fill(BLACK, opacity=0)
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

def playArcSwap(self, element1, element2, arc=180):
    element1_copy = element1.copy().shift(element2.get_center()-element1.get_center())
    element2_copy = element2.copy().shift(element1.get_center()-element2.get_center())
    self.play(Transform(element1, element1_copy, path_arc = arc * DEGREES), Transform(element2, element2_copy, path_arc = arc * DEGREES), run_time=0.75)

def highlight(self, color, item, color2, *items):
    self.play(FadeToColor(item, color), FadeToColor(*items, color2), run_time=0.75)

def createGraph(node):
    return VGroup().add(node)

def addNodeToGraph(graph, graph_node, new_node, x_offset, y_offset, buffer):
    new_node = new_node.shift(graph_node.get_center() + RIGHT * x_offset + DOWN * y_offset)
    graph.add(new_node).add(Line(start=graph_node[0], end=new_node[0], buff=buffer).add_tip())

def createArray(element):
    return VGroup().add(element)

def addToArrayVertical(array, element):
    array.add(element.shift(array[-1].get_center() + DOWN))

def addToArrayHorizontal(array, element):
    array.add(element.shift(array[-1].get_center() + RIGHT))

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

def updateText(self, text, new_text):
    self.play(FadeOut(text), FadeIn(new_text), run_time = 0.4)
    self.wait(0.4)

class BubbleSort(Scene):
    def construct(self):
        intro_words = Text("""What is Bubble Sort?""").to_edge(UP).scale(1.2)

        current_step = Text("""Current Step""").to_edge(DOWN).scale(0.8)
        current_step_increment = Text("""increment current and next indices""").to_edge(DOWN).scale(0.8)
        current_step_correct_order = Text("""correct order of current and next element""").to_edge(DOWN).scale(0.8)
        current_step_restart = Text("""restart if you swapped""").to_edge(DOWN).scale(0.8)
        current_step_finished = Text("""did not swap, so array is sorted""").to_edge(DOWN).scale(0.8)

        did_swap_false = Text("""swapped == false""").shift(UP * 2 + RIGHT * 3).scale(0.8)
        did_swap_true = Text("""swapped == true""").shift(UP * 2 + RIGHT * 3).scale(0.8)

        array = createArray(createRectangleNode(4, 1, 1)).shift(LEFT * 2 + DOWN * 1)
        addToArrayHorizontal(array, createRectangleNode(5, 1, 1))
        addToArrayHorizontal(array, createRectangleNode(2, 1, 1))
        addToArrayHorizontal(array, createRectangleNode(1, 1, 1))
        addToArrayHorizontal(array, createRectangleNode(3, 1, 1))

        current_label = Text("current", t2c={"current": RED}).shift(UP + LEFT * 2).scale(0.8)
        current_label_line = Line(current_label, array[0], buff=0.2).add_tip()
        current_label_group = VGroup().add(current_label).add(current_label_line)
        next_label = Text("next", t2c={"next": BLUE}).shift(UP + LEFT).scale(0.8)
        next_label_line = Line(next_label, array[1], buff=0.2).add_tip()
        next_label_group = VGroup().add(next_label).add(next_label_line)

        current_overlay = Square(1, stroke_width=0).shift(array[0].get_center()).set_fill(RED, opacity=0.4)
        next_overlay = Square(1, stroke_width=0).shift(array[1].get_center()).set_fill(BLUE, opacity=0.4)
        overlay_group = VGroup().add(current_overlay).add(next_overlay)

        self.play(Write(intro_words), Write(array), Write(current_step), Write(did_swap_false))
        self.play(Write(current_label_group), FadeIn(current_overlay))
        self.wait(0.5)
        current_label.generate_target()
        current_label.target.shift(UP)
        self.play(FadeOut(current_label_group[1]), MoveToTarget(current_label), Write(next_label_group), FadeIn(next_overlay), run_time=0.5)
        self.wait(0.5)
        next_label.generate_target()
        next_label.target.shift(LEFT + UP * 0.5)
        self.play(FadeOut(next_label_group[1]), MoveToTarget(next_label), run_time=0.5)


        #iteration 1
        updateText(self, current_step, current_step_correct_order)

        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.generate_target()
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)
        playArcSwap(self, array[1], array[2])
    
        updateText(self, did_swap_false, did_swap_true)

        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)
        playArcSwap(self, array[1], array[3])

        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)
        playArcSwap(self, array[1], array[4])

        updateText(self, current_step_correct_order, current_step_restart)

        #iteration 2
        overlay_group.generate_target()
        overlay_group.target.shift(LEFT * 3)
        self.play(MoveToTarget(overlay_group), run_time=0.75)
        updateText(self, did_swap_true, did_swap_false)

        updateText(self, current_step_restart, current_step_correct_order)
        playArcSwap(self, array[0], array[2])
        updateText(self, did_swap_false, did_swap_true)


        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.generate_target()
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)
        playArcSwap(self, array[0], array[3])
    
        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)
        playArcSwap(self, array[0], array[4])

        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)

        updateText(self, current_step_correct_order, current_step_restart)


        #iteration 3
        overlay_group.generate_target()
        overlay_group.target.shift(LEFT * 3)
        self.play(MoveToTarget(overlay_group), run_time=0.75)
        updateText(self, did_swap_true, did_swap_false)

        updateText(self, current_step_restart, current_step_correct_order)
        playArcSwap(self, array[2], array[3])
        updateText(self, did_swap_false, did_swap_true)

        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.generate_target()
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)
    
        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)

        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)

        updateText(self, current_step_correct_order, current_step_restart)

        #iteration 4
        overlay_group.generate_target()
        overlay_group.target.shift(LEFT * 3)
        self.play(MoveToTarget(overlay_group), run_time=0.75)
        updateText(self, did_swap_true, did_swap_false)

        updateText(self, current_step_restart, current_step_correct_order)

        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.generate_target()
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)
    
        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)

        updateText(self, current_step_correct_order, current_step_increment)
        overlay_group.target.shift(RIGHT)
        self.play(MoveToTarget(overlay_group), run_time=0.75)

        updateText(self, current_step_increment, current_step_correct_order)

        updateText(self, current_step_correct_order, current_step_restart)

        updateText(self, current_step_restart, current_step_finished)
        self.wait(0.5)
        array.generate_target()
        array.target.scale(1.2)
        self.play(FadeOut(overlay_group), FadeOut(current_step_finished), MoveToTarget(array))
        self.wait(1)