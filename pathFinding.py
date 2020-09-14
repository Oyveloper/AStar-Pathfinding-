from maps import Map_Obj
from searching import AStar, Node
import sys


# THis is the main execution script for this Assigment
# To run a task simply run python3 pathFinding n
# where n is the task number you want

# Retrieves the task to run from the script input
args = sys.argv
task = 1
if len(args) > 1:
    task = int(args[1])

samf_map = Map_Obj(task=task)

# Get the goal node from my A* implementation 
goal_node: Node = AStar(samf_map)

# Show the map for the problem
samf_map.show_map()

# Mark each state that the A* algorithms
# says is part of the solution
# Wokring bakward from the end node, marking the parent
previous: Node = goal_node
while previous is not None:
    samf_map.set_cell_value(previous.get_position(), None, samf_map.get_goal_pos())
    previous = previous.get_previous()

# Need to reset the start and end markers after overwriting
# in the loop above 
samf_map.set_start_pos_str_marker(samf_map.get_start_pos(), samf_map.str_map)
samf_map.set_goal_pos_str_marker(samf_map.get_goal_pos(), samf_map.str_map)

# show the solution
samf_map.show_map()
