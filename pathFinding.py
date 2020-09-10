from maps import Map_Obj
from searching import AStar, Node

import sys

args = sys.argv
task = 1
if len(args) > 1:
    task = int(args[1])

samf_map = Map_Obj(task=task)
goal_node: Node = AStar(samf_map)


samf_map.show_map()

previous: Node = goal_node
while previous is not None:
    samf_map.set_cell_value(previous.get_position(), None, samf_map.get_goal_pos())
    previous = previous.get_previous()

samf_map.set_start_pos_str_marker(samf_map.get_start_pos(), samf_map.str_map)
samf_map.set_goal_pos_str_marker(samf_map.get_goal_pos(), samf_map.str_map)
samf_map.show_map()

