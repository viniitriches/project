The class file ThePlayer has the implementation of two players: TheISDPlayer and TheAStarPlayer. The first one uses the algorithm iterative deepening search, that expands the first node that was added to the stack, and the second astar, that expands the node with the lowest cost (path cost + heuristic).

The array with the food locations is first sorted according to the proximity of each food to the eater location. Then for each of these an initial state is created with the eater location and the food location, a goal state with the location of the food as the eater location, and a problem that receives information about the world, the initial state and the goal state.

After the search algorithm returns the solution to this partial problem, the eater location is updated to its last location, which corresponds to the current food location.

The file search_utils/search_problem.py contains the implementation of the EaterProblem, EaterState and Node classes. The Node class was already almost completely implemented in the files provided by the professor.

The file search_utils/search_algorithm contains the implementation of the search algorithms. The Frontier classes were already implemented.

Run in the lab01-magenta directory:

gridrunner --world EaterWorld --entry the_player:TheIDSPlayer search/data/eater-world_0.json

and 

gridrunner --world EaterWorld --entry the_player:TheAStarPlayer search/data/eater-world_0.json

world 0
TheIDSPlayer   0.06s user 0.02s system 93% cpu 0.093 total
TheAStarPlayer   0.06s user 0.02s system 93% cpu 0.092 total

world 1
TheIDSPlayer   0.18s user 0.06s system 70% cpu 0.329 total
TheAStarPlayer   0.07s user 0.02s system 94% cpu 0.096 total

world 2
TheIDSPlayer   10.61s user 0.04s system 99% cpu 10.687 total
TheAStarPlayer   0.11s user 0.05s system 59% cpu 0.267 total