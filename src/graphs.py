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


graph = Graph([(0,2), (4,6), (4,8), (4,0), (3,1), (0,3), (3,5), (5,7), (3,9), (3,10)])
print(graph.num_edges)
print(graph.get_children(3))
print(graph.get_parents(4))
        