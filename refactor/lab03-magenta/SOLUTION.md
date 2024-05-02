1)
Puzzle:
    FF:
	    cost: 241
	    time: 0.152346s
	    expanded states: 2753
	    generated states: 8807


    Additive:
	    cost: 187
	    time: 0.137337s
	    expanded states: 1443
	    generated states: 5307

    Blind:
	    did not finish


Weighted:
    FF:
	    cost: 268
	    time: 0.169434s
	    expanded states: 3550
	    generated states: 11106


    Additive:
	    cost: 496
	    time: 0.408589s
	    expanded states: 6059
	    generated states: 21551

    Blind:
	    did not finish

Puzzle Glued:
    FF:
	    cost: 589
	    time: 6.06344s
	    expanded states: 229859
	    generated states: 634659

    Additive:
	    cost: 657
	    time: 54.793s
	    expanded states: 2005642
	    generated states: 5926523

    Blind:
	    did not finish

Puzzle Cheat:
    FF:
	    cost: 13
	    time: 0.234443s
	    expanded states: 14
	    generated states: 231

    Additive:
	    cost: 13
	    time: 0.148839s
	    expanded states: 14
	    generated states: 231

    Blind:
	    did not finish

2.
When the light is toggled we move the agents according to the specifications and when they meet they start to fight. Who wins is also decided according to the specifications. Conditionals were used to cover all cases.

3.a) For the wumpus exercise, I modeled the wumpus structure to pddl with all the actions available. For the cost attribute, I used the function explained and the domain takes the action costs from the problem. The simple configuration works well.

3.b) The python code has already a little explanation and comments on it, it will write all the basic configurations and take the parameters that can change such as agent, gold, wumpus and pit and store its location. The initialization and goal can be modified as needed. It creates a file with "wumpus-problem.pddl" as the name and prints the location.

3.c) After running the heuristics available, it is noticeable that the "ff", "add" and "cea" heuristics have a very similar outcome (most times equal) and tend to be the most efficient. Other heuristics such as "context-enhanced additive" and "blind" also work but with varying outcomes, sometimes positive and sometimes negative.
