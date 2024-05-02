import random
from wumpus import WumpusWorld, Coordinate
from pathlib import Path

"""
    As parameters I will use the following:
    - world_instance: An instance of the WumpusWorld class from the wumpus package given.
    - output_file_path: The path to save the generated PDDL problem file.
"""
def create_wumpus_pddl_problem(world_instance, output_file_path):
    # I will use the with statement to open the file and write the lines needed for the PDDL problem file with
    #  wumpus-problem as the name of the problem file and wumpus-domain as the name of the domain file
    with open(output_file_path, 'w') as f:
        # I will write all the lines needed for the header and objects. The initial state and the goal
        # can be modified as needed
        f.write("(define (problem wumpus-problem)\n")
        f.write("  (:domain wumpus-domain)\n")
        f.write("  \n(:requirements :action-costs)\n")
        f.write("  \n(:objects\n")

        agent_location = world_instance.agent_locations['agent']
        gold_location = world_instance.gold_locations['gold']
        wumpus_location = world_instance.wumpus_locations['wumpus']
        pit_locations = world_instance.pit_locations['pit']
        f.write(f"    agent\n")
        f.write(f"    arrow\n")
        for x in range(world_instance.size[0]):
            for y in range(world_instance.size[1]):
                cell = f"sq-{x}-{y}"
                if Coordinate(x, y) == world_instance.gold_locations['gold']:
                    f.write(f"    gold\n")
                if Coordinate(x, y) == world_instance.wumpus_locations['wumpus']:
                    f.write(f"    wumpus\n")
                if Coordinate(x, y) == world_instance.pit_locations['pit']:
                    f.write(f"    pit\n")
                f.write(f"    {cell}\n")
        f.write("  )\n")

        # Other initial state necessities can be added here
        f.write("  (:init\n")
        agent_location_str = f"sq-{agent_location[0]}-{agent_location[1]}"
        gold_location_str = f"sq-{gold_location[0]}-{gold_location[1]}"
        wumpus_location_str = f"sq-{wumpus_location[0]}-{wumpus_location[1]}"
        pit_location_str = f"sq-{pit_locations[0]}-{pit_locations[1]}"
        f.write(f"    (at agent {agent_location_str})\n")
        f.write(f"    (at gold {gold_location_str})\n")
        f.write(f"    (at wumpus {wumpus_location_str})\n")
        f.write(f"    (at pit {pit_location_str})\n")
        f.write(f"    (arrow-is arrow)\n")
        f.write(f"    (agent-is agent)\n")
        f.write(f"    (takeable gold)\n")
        f.write(f"    (have agent arrow)\n")
        f.write(f"    (exit-is sq-0-0)\n")
        f.write(f"    (= (total-cost) 0)\n")

        for x in range(world_instance.size[0]):
            for y in range(world_instance.size[1]):
                cell = f"sq-{x}-{y}"
                if Coordinate(x, y) == world_instance.gold_locations['gold']:
                    f.write(f"    (gold-is gold)\n")
                if Coordinate(x, y) == world_instance.wumpus_locations['wumpus']:
                    f.write(f"    (wumpus-is wumpus)\n")
                if Coordinate(x, y) == world_instance.pit_locations['pit']:
                    f.write(f"    (pit-is pit)\n")
                adjacent_cells = [
                (x, y + 1) if y + 1 < world_instance.size[1] else None,  # Above
                (x, y - 1) if y - 1 >= 0 else None,  # Below
                (x + 1, y) if x + 1 < world_instance.size[0] else None,  # Right
                (x - 1, y) if x - 1 >= 0 else None,  # Left
                ]
                for adj_coords in adjacent_cells:
                    if adj_coords is not None:
                        adj_x, adj_y = adj_coords
                        adj_cell = f"sq-{adj_x}-{adj_y}"
                        f.write(f"    (adj {cell} {adj_cell})\n")
            
        f.write("  )\n")

        # The goal can be modified as needed
        f.write("  (:goal\n")
        f.write("    (and (have agent gold) (did-climb)))\n")

        f.write("  \n(:metric minimize (total-cost))\n")
        f.write(")\n")

if __name__ == "__main__":
    # Create a sample Wumpus World instance, set a basic initial state, and create the PDDL problem file

    # The parameters for WumpusWorld
    world_size = (4, 4)
    blocked_cells = []
    world_instance = WumpusWorld(size=world_size, blocks=blocked_cells)

    # Set a basic initial state
    world_instance.agent_locations = {'agent': (0, 0)}
    world_instance.gold_locations = {'gold': Coordinate(random.randint(0, 3), random.randint(0, 3))}
    world_instance.wumpus_locations = {'wumpus': Coordinate(random.randint(1, 3), random.randint(0, 3))}
    world_instance.pit_locations = {'pit': Coordinate(random.randint(1, 3), random.randint(1, 3))}

    current_file_path = Path(__file__)
    output_path = current_file_path.parent / "wumpus-problem.pddl"

    create_wumpus_pddl_problem(world_instance, output_path)

    print(f"PDDL problem file created: {output_path}")
    print(f"Output file path: {output_path}")
