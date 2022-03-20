
from stack_queue import *

class Node: 

    def __init__(self, index): 
        self.index = index
        self.distance = 0
        self. previous = None
    

class Graph: 

    def __init__(self, edges): 
        self.edges = edges
        self.num_edges = len(edges)

        self.nodes = {}
        self.parents_by_node = {}
        for edge in edges:
            if edge[0] not in self.nodes:
                self.nodes[edge[0]] = Node(edge[0])
            if edge[1] not in self.nodes:
                self.nodes[edge[1]] = Node(edge[1])
        
        self.parents_by_node = {}
        self.children_by_node = {}
        for nodes in self.nodes: 
            self.parents_by_node[nodes] = self.get_parents(nodes)
            self.children_by_node[nodes] = self.get_children(nodes)
        
        
    def get_children(self, node): 
        children = []
        for i in range(self.num_edges): 
            if self.edges[i][0] == node:
                children.append(self.edges[i][1])
       
        return children
    
    def get_parents(self, node): 
        parents = []
        for i in range(self.num_edges): 
            if self.edges[i][1] == node: 
                parents.append(self.edges[i][0])

        return parents
    
    def breadth_first(self, node): 
        queue = Queue()
        queue.enqueue(node)
        visited = {}
        order = []
        while len(queue.items) != 0:
            current_node = queue.items[0]
            order.append(current_node)
            visited.update({current_node: True})
            queue.dequeue()

            children = self.get_children(current_node)

            for child in children:
                if child in visited:
                    continue
                queue.enqueue(child)
                visited.update({child: True})
        return order 

    def depth_first(self, node): 
        
        stack = Stack()
        stack.push(node)
        visited = {}
        order = []
        while len(stack.elements) != 0:
            current_node = stack.elements[-1]
            order.append(current_node)
            visited.update({current_node: True})
            stack.pop()
            children = self.get_children(current_node)

            for child in children:
                if child in visited:
                    continue
                stack.push(child)
                visited.update({child: True})
        return order 
    
    def set_distance_and_previous(self, start_index):
        queue = Queue()
        queue.enqueue(start_index)
        visited = {}
        order = [start_index]
        while len(queue.items) != 0:
        
            current_node = queue.items[0]
            order.append(current_node)
            visited.update({current_node: True})
            queue.dequeue()
            children = self.get_children(current_node)
            node = self.nodes[current_node]

            for child in children:
                if child in visited:
                    continue
                self.nodes[child].previous = current_node
                self.nodes[child].distance = self.nodes[current_node].distance + 1
                queue.enqueue(child)
                visited.update({child: True})
        return order 
    
    def calc_distance(self, start_index, ending_index):
        self.set_distance_and_previous(start_index)
        if ending_index not in self.set_distance_and_previous(start_index):
            return False
        else: 
            return self.nodes[ending_index].distance
    
    def calc_shortest_path(self, start_index, ending_index): 
        self.set_distance_and_previous(start_index)

        if self.calc_distance(start_index, ending_index) == False: 
            return False 
        
        shortest_path = []
        start_node_index = start_index
        current_node_index = ending_index
        while current_node_index != start_node_index: 
            shortest_path.append(current_node_index)
            current_node_index = self.nodes[current_node_index].previous
            shortest_path.append(current_node_index)

        shortest_path = list(dict.fromkeys(shortest_path))
        return shortest_path[::-1]


