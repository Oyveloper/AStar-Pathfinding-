#!/usr/bin/env python3
from .Node import Node

class Frontier(object):
    def __init__(self):
        self.frontier_list = []

    def get_next(self) -> Node:
        """Returns the node with the lowest expected cost"""
        next_node: Node = self.frontier_list[0]
        node: Node
        for node in self.frontier_list:
            if node.get_expected_cost() < next_node.get_expected_cost():
                next_node = node

        self.frontier_list.remove(next_node)
        return next_node

    def add_node(self, node: Node):
        """Adds the node to the frontier"""
        self.frontier_list.append(node)

    def is_empty(self):
        return len(self.frontier_list) == 0

    def contains_node(self, node: Node) -> bool:
        """Returns true if the node is present in the frontier"""
        return node in self.frontier_list

    def get_node(self,  node: Node) -> Node:
        return self.frontier_list[self.frontier_list.index(node)]
