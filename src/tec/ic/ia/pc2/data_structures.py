"""
Data structures module
"""

import heapq


class PriorityQueue:
    """ Priority Queue Data Structure """

    def __init__(self):
        self.elements = []

    def empty(self):
        """
        Returns if the queue is empty
        """
        size = len(self.elements)
        return size == 0

    def push(self, element, priority):
        """
        Inserts an element to the queue
        """
        heapq.heappush(self.elements, (priority, element))

    def pop(self):
        """
        Pops an element from the queue
        """
        return heapq.heappop(self.elements)[1]


class Node:
    """ Node Data Structure """

    def __init__(self, key, carrot=False):
        self.key = key
        self.incoming_edges = 0
        self.carrot = carrot
        self.h_cost = 0
        self.g_cost = 0
        self.adj_nodes = {}

    def consume_carrot(self):
        """
        Bunny eats the carrot
        """
        consumed_carrot = False
        if self.carrot:
            self.carrot = False
            consumed_carrot = True
        return consumed_carrot

    def add_neighbor(self, neighbor):
        """
        Adds a neighbor with the given weight in the link
        """
        if neighbor is None:
            raise TypeError('neighbor or weight cannot be None')
        neighbor.incoming_edges += 1
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        """
        Removes a neighbor
        """
        if neighbor is None:
            raise TypeError('neighbor cannot be None')
        if neighbor.key not in self.adj_nodes:
            raise KeyError('neighbor not found')
        neighbor.incoming_edges -= 1
        del self.adj_nodes[neighbor.key]


class Graph:
    """ Graph Data Structure """

    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        """
        Adds a node to the graph
        """
        if key is None:
            raise TypeError('key cannot be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key):
        """
        Conects to nodes of the graph
        """
        if source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key])

    def neighbors(self, key):
        """
        Gets all node's neighbors
        """
        return self.nodes[key].adj_nodes

    def get_scope_keys(self, key, depth=1):
        """
        Gets all the node keys within the depth based scope
        """
        result = []
        keys = [key]
        while depth > 0:
            for node in keys:
                neighbors = list(self.neighbors(node).keys())
                res = set(result)
                subres = set(keys)
                nested = set(neighbors)
                without_repetition = nested - res
                result = result + list(without_repetition)
                without_repetition = nested - subres
                keys = keys + list(without_repetition)
            depth -= 1
        if key in result:
            result.remove(key)
        return result

    def __str__(self):
        string = ""
        for key in self.nodes:
            string += str(key) + ' - '
        return string[:-3]
