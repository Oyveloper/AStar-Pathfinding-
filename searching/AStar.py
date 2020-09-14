from .Node import Node
from maps import Map_Obj

import queue


def AStar(map_obj: Map_Obj) -> Node:
    """
    Implementation fo the A* algorithm
    Returns an optimal solution for finding the path from the start_node to the end_node
    this is returned as the end node which holds information about the path
    """

    # Defines the starting position as a node
    # This is found from the Map_Object
    start_node = Node(map_obj.get_start_pos())
    
    end_position = map_obj.get_end_goal_pos()

    # Use built in, efficient priority queue as the frontier 
    frontier = queue.PriorityQueue()

    # Keep track of all the explored nodes in a map for fast lookup
    # i.e. this is a graph search version of A*
    explored: {str: Node} = {}

    # Keep track of the nodes that are generated in a map
    # for fast lookups. Modifying elements here will update
    # them in frontier and explored as wel 
    generated_nodes: {str: Node} = {}

    # Start the algorithm by adding the initial node to the frontier
    frontier.put(start_node)

    goal_node = None

    # Run the algorithm as long as the frontier is not empty
    while not frontier.empty():
        # Get the next node
        current_node: Node = frontier.get()

        # Goal check
        # (Important to do this on exploration and not generation)
        if current_node.get_position() == tuple(end_position):
            goal_node = current_node
            break

        # Get all the positions for possible children
        children: [Node] = expand(current_node, map_obj)
        explored[key_for_node(current_node)] = current_node

        # generate the child nodes
        child: Node
        for child in children:
            # If this node has been generated before, get the
            # already generated one so it can be updated in case
            # the new cost is lower
            if key_for_node(child) in generated_nodes:
                child = generated_nodes[key_for_node(child)]
            else:
                generated_nodes[key_for_node(child)] = child

            # Only add as child if it is not explored yet
            if key_for_node(child) not in explored:
                current_node.add_child(child)

            # Calculate the cost when comming from the current node
            cost_via_current_node = (
                current_node.get_cost() +
                map_obj.get_cell_value((child.get_position()))
            )

            # UPdate the cost if it is better (or if it has no cost yet)
            if child.get_previous() is None or cost_via_current_node < child.get_cost():
                child.set_previous(current_node)
                child.set_cost(cost_via_current_node)

            if key_for_node(child) not in explored:
                frontier.put(child)

    return goal_node


def expand(node: Node, map_obj: Map_Obj) -> [Node]:
    """Finds all possible positions to walk to given the current node
    Returns as Node object
    """
    position: (int, int) = node.position

    nodes: [Node] = []

    # left, right, up, down
    possible_positions = [
        (position[0] - 1, position[1]),
        (position[0] + 1, position[1]),
        (position[0], position[1] - 1),
        (position[0], position[1] + 1),
    ]

    for pos in possible_positions:
        # Might throw an error if we index outside the map
        # but we just catch and ignore those errors
        try:
            # Don't accept walls
            if map_obj.get_cell_value(pos) != -1:
                node.set_heuristic(heuristic(node, map_obj))
                nodes.append(Node(pos))
        except Exception:
            # Position outside map
            continue

    return nodes


def key_for_node(node: Node) -> str:
    """Sort of a hashing function for
    nodes giving a unique key to put in map"""
    return f"{node.position[0]},{node.position[1]}"


def heuristic(node: Node, map_obj: Map_Obj) -> float:
    """
    The heuristic function for each node
    We here use the manhattan distance from the
    current node to the goal_node
    """

    goal_position = map_obj.get_end_goal_pos()
    node_position = node.get_position()

    return abs(goal_position[0] - node_position[0]) + abs(goal_position[1] - node_position[1])
