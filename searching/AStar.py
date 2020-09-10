from .Node import Node
from maps import Map_Obj
from .Frontier import Frontier

def AStar(map_obj: Map_Obj) -> Node:
    """
    Implementation fo the A* algorithm
    Returns an optimal solution for finding the path from the start_node to the end_node
    this is returned as the end node which holds information about the path
    """
    start_node = Node(map_obj.get_start_pos())
    end_position = map_obj.get_end_goal_pos()

    frontier:Frontier = Frontier()
    explored: [Node] = []
    frontier.add_node(start_node)

    while not frontier.is_empty():
        current_node: Node = frontier.get_next()

        if current_node.get_position() == tuple(end_position):
            # We have found the solution
            return current_node

        children: [Node] = expand(current_node, map_obj)
        explored.append(current_node)

        child: Node
        for child in children:

            # If this node has been generated before, get the already generated one
            if frontier.contains_node(child):
                child = frontier.get_node(child)


            current_node.add_child(child)

            cost_via_current_node = current_node.get_cost() + map_obj.get_cell_value((child.get_position()))

            if child.get_previous() is None or cost_via_current_node < child.get_cost():
                    child.set_previous(current_node)
                    child.set_cost(cost_via_current_node)


            
            if not child in explored:
                frontier.add_node(child)

    print(end_position)


def expand(node: Node, map_obj: Map_Obj) -> [Node]:
    position: (int, int) = node.position

    nodes: [Node] = []

    possible_positions = [
        (position[0] - 1, position[1]),
        (position[0] + 1, position[1]),
        (position[0], position[1] - 1),
        (position[0], position[1] + 1),
    ]

    for pos in possible_positions:
        try:
            if map_obj.get_cell_value(pos) != -1:
                node.set_heuristic(heuristic(node, map_obj))
                nodes.append(Node(pos))
        except Exception as e:
            # Position outside map
            continue

    return nodes


def heuristic(node: Node, map_obj: Map_Obj) -> float:
    """
    The heuristic function for each node
    We here use the manhattan distance from the
    current node to the goal_node
    """

    goal_position = map_obj.get_end_goal_pos()
    node_position = node.get_position()

    return abs(goal_position[0] - node_position[0]) + abs(goal_position[1] - node_position[1])
