from stack_queue import *

class Graph: 

    def __init__(self, edges): 
        self.edges = edges
        self.num_edges = len(self.edges)
    
    def get_children(self, parent): 
        children = []
        for i in range(self.num_edges): 
            if self.edges[i][0] == parent:
                children.append(self.edges[i][1])
        return children
    
    def get_parents(self, child): 
        parents = []
        for i in range(self.num_edges): 
            if self.edges[i][1] == child: 
                parents.append(slef.edges[i][0])
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

        

        