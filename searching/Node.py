class Node(object):
    """Represents a single node in the search graph"""

    def __init__(self, position: (int, int)):
        self.position = position
        self.cost = 0
        self.heuristic = 0
        self.previous = None
        self.children = []

    def set_cost(self, cost: int):
        difference = self.cost - cost
        self.cost = cost

        # Propagate the change in cost down to all children
        child: 'Node'
        for child in self.children:
            if child.get_previous() == self:
                child.set_cost(child.get_cost() - difference)

    def get_cost(self):
        return self.cost

    def set_heuristic(self, heuristic: int):
        self.heuristic = heuristic

    def get_expected_cost(self):
        return self.cost + self.heuristic

    def set_previous(self, node: 'Node'):
        self.previous = node

    def get_previous(self) -> 'Node':
        return self.previous

    def get_position(self) -> (int, int):
        return self.position

    def add_child(self, node: 'Node'):
        self.children.append(node)

    # The following methods are implemented so I
    # can use a priority queue for the frontier
    def __eq__(self, o: 'Node'):
        """Enables simple comparrison between two node objects
        This makes it possible to compare newly generated nodes
        to old ones, even though they aren't the same object in
        memory"""
        return self.get_expected_cost() == o.get_expected_cost()

    def __lt__(self, o: 'Node'):
        return self.get_expected_cost() < o.get_expected_cost()

    def __le__(self, o: 'Node'):
        return self.get_expected_cost() <= o.get_expected_cost()

    def __ne__(self, o: 'Node'):
        return self.get_expected_cost() != o.get_expected_cost()

    def __gt__(self, o: 'Node'):
        return self.get_expected_cost() > o.get_expected_cost()

    def __ge__(self, o: 'Node'):
        return self.get_expected_cost() >= o.get_expected_cost()
        

