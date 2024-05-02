from .search_problem import Node, is_in
from .priority_queue import *

def iterative_deepening_search(problem):
    for depth in range(1000):
        result = depth_limted_search(problem, depth)
        if result is not None:
            return result
        
def depth_limted_search(problem, l):
    frontier = StackFrontier([Node(problem.initial)])
    result = None
    while not frontier.is_empty():
        node = frontier.select_and_remove()
        if problem.goal_test(node.state):
            return node
        if node.depth > l:
            result = None
        else:
            for child in node.expand(problem):
                frontier.add(child)
    return result

def astar_search(problem):
    return graph_search(problem, PriorityQueueFrontier([Node(problem.initial)],
                                                       lambda node: node.path_cost + problem.h(node)))

def graph_search(problem, frontier):
    """
    A generic search algorithm, with loop detection. Frontier must already be initialized to problem.initial (the initial node)
    """
    explored_states = set()
    while not frontier.is_empty():
        node = frontier.select_and_remove()
        print(node.state.eater_location)
        if problem.goal_test(node.state):
            return node
        explored_states.add(node.state)
        for n in node.expand(problem):
            if (n.state not in explored_states) and (not frontier.contains(n)):
                frontier.add(n)
    return None

class Frontier:
    """The generic interface of a frontier for a search algorithm."""
    def __init__(self, elements):
        raise NotImplementedError

    def select_and_remove(self):
        raise NotImplementedError

    def contains(self, node):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def add_all(self, elements):
        raise NotImplementedError

    def add(self, element):
        raise NotImplementedError


class StackFrontier(Frontier):
    """Implements the frontier as a stack"""
    def __init__(self, elements):
        self.stack = elements

    def select_and_remove(self):
        return self.stack.pop()

    def contains(self, node):
        return is_in(node, self.stack)

    def is_empty(self):
        return self.stack == []

    def add_all(self, elements):
        self.stack += elements

    def add(self, element):
        self.stack.append(element)

    def __repr__(self):
        return str(self.stack)
    
class PriorityQueueFrontier(Frontier):
    """ Implements the frontier as a priority queue """
    def __init__(self, elements_list, cost_function):
        self.pq = PriorityQueue('min', cost_function)
        for n in elements_list:
            self.pq.append(n)

    def select_and_remove(self):
        return self.pq.pop()

    def contains(self, node):
        return self.pq.__contains__(node)

    def is_empty(self):
        return self.pq.__len__() == 0

    def add_all(self, elements):
        for node in elements:
            self.pq.append(node)

    def add(self, element):
        self.pq.append(element)

    def __repr__(self):
        return str(self.pq.heap)