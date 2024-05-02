from wumpus import Eater, coord, Coordinate
from typing import Iterable

def is_in(elt, seq):  # Utility function
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)


class Problem:
    """The abstract class for a formal problem. You should subclass this and implement the methods and
    actions and result, and possibly __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action): # The result of applying an action
        raise NotImplementedError

    def goal_test(self, state):
        if isinstance(self.goal, list):
            return self.is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
       return c + 1

class EaterProblem(Problem):
    #represents the problem to be solved
    def __init__(self, initial, goal, block_locations: Iterable[Coordinate], world_dimension: Coordinate):
        self.initial = initial
        self.goal = goal
        self.block_locations = block_locations
        self.world_dimension = world_dimension

    #returns the available actions for a given state
    def actions(self, state):
        available_actions = []
        for action in Eater.Actions:
            delta = action.value
            new_pos = coord(state.eater_location.x + delta[0], state.eater_location.y + delta[1])

            if is_valid_position(new_pos, self.block_locations, self.world_dimension):
                available_actions.append(action)

        return available_actions

    #returns the result (new state) of applying an action in a given state
    def result(self, state, action):
        new_food_locations = state.food_locations.copy()

        delta = action.value
        new_eater_location = coord(state.eater_location.x + delta[0], state.eater_location.y + delta[1])

        if new_eater_location == state.food_locations[0]:
            print('found banana')
            new_food_locations.pop(0)
            # if len(new_food_locations) > 0:
            #     new_food_locations.sort(key = lambda food_location : manhattan_distance(new_eater_location, food_location))

        new_state = EaterState(new_eater_location, new_food_locations)
        return new_state

    #tests if a given state corresponds to the goal state
    def goal_test(self, state):
        return len(state.food_locations) == 0

    def path_cost(self, c):
       return c + 1
    
    def h(self, node):
        if len(node.state.food_locations) > 0:
            return manhattan_distance(node.state.eater_location, node.state.food_locations[0])
        else: return 0

def is_valid_position(new_pos, blocks, dimension):
    return new_pos not in blocks and new_pos.x >= 0 and new_pos.x < dimension.x and new_pos.y >= 0 and new_pos.y < dimension.y
    
def manhattan_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

class EaterState:
    #represents states during the solution of a problem
    #in this case a state is comprised by the location of the eater (player) and the location of the foods
    def __init__(self, eater_location: Coordinate, food_locations: list[Coordinate]):
        self.eater_location = eater_location
        self.food_locations = food_locations

class Node:
    """
    A node in the search tree
    """
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action # action from parent to this node
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        result = "["
        for node in self.path():
            result += "<Node {}>".format(node.state)
        result += "]" + ", cost = " + str(self.path_cost)
        return result

    def __lt__(self, node):
        return self.path_cost < node.path_cost

    def expand(self, problem):
        return [self.child_node(problem, action)
            for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost))
        return next_node

    # Returns the actions taken to arrive to the goal state
    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)
    


    