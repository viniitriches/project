from wumpus import OfflinePlayer, Eater, EaterWorld, Food
from typing import Iterable
from search_utils.search_algorithms import iterative_deepening_search, astar_search
from search_utils.search_problem import EaterProblem, EaterState, manhattan_distance

#does it make sense to separe the problem in subproblems where each is to find the path to a food location?
#why does it not work for world 3? it finds the first two foods and then gets stuck

class TheIDSPlayer(OfflinePlayer):
    
    def start_episode(self, world: EaterWorld) -> Iterable[Eater.Actions]:
        print('Episode starting')

        # inspect the objects in the world
        food_locations = []
        eater_location = None
        for o in world.objects:
            if isinstance(o, Eater):
                eater_location = o.location
            elif isinstance(o, Food):
                food_locations.append(o.location)

        solution = []

        for food_location in food_locations:
            initial = EaterState(eater_location, food_locations)
            goal = EaterState(None, [])
            problem = EaterProblem(initial, goal, world.blocks, world.size)

            result = iterative_deepening_search(problem)
            solution.extend(result.solution())

            #update eater location
            eater_location = food_location

        return solution
    
    def end_episode(self, outcome: int, alive: bool, success: bool):
        print('Episode completed, my reward is {}'.format(outcome))

# gridrunner --world EaterWorld --entry the_player:TheIDSPlayer search/data/eater-world_0.json

            
class TheAStarPlayer(OfflinePlayer):

    def start_episode(self, world: EaterWorld) -> Iterable[Eater.Actions]:
        print('Episode starting')

        # inspect the objects in the world
        food_locations = []
        eater_location = None
        for o in world.objects:
            if isinstance(o, Eater):
                eater_location = o.location
            elif isinstance(o, Food):
                food_locations.append(o.location)

        food_locations.sort(key = lambda food_location : manhattan_distance(eater_location, food_location))

        solution = []

        initial = EaterState(eater_location, food_locations)
        goal = EaterState(None, [])
        problem = EaterProblem(initial, goal, world.blocks, world.size)

        result = astar_search(problem)
        solution.extend(result.solution())
                    
        return solution
    
    def end_episode(self, outcome: int, alive: bool, success: bool):
        print('Episode completed, my reward is {}'.format(outcome))


# gridrunner --world EaterWorld --entry the_player:TheAStarPlayer search/data/eater-world_0.json