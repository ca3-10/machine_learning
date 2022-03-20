import sys
sys.path.append('src')
from graphs import Graph

graph = Graph([(4, 0), (4, 8), (4, 6), (0, 8), (0, 2), (0, 3), (6, 3), (3, 2), (2, 3), (3, 1), (3, 5), (3, 9), (5, 7)])
graph_2 = Graph([(0, 1),(0, 2), (0, 3), (1, 2), (2, 3), (3, 4), (3, 5), (3, 6), (6, 7), (6, 8)])
graph_3 = Graph([(0,1), (1,4), (1,2), (4,3), (4,5), (3,6), (3,1)])

#BFS
assert graph.breadth_first(4) == [4, 0, 8, 6, 2, 3, 1, 5, 9, 7]
assert graph.breadth_first(3) == [3, 2, 1, 5, 9, 7]
assert graph_2.breadth_first(0) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
assert graph_2.breadth_first(8) == [8]\

#DFS 
assert graph.depth_first(4) == [4, 6, 3, 9, 5, 7, 1, 2, 8, 0]
assert graph.depth_first(3) == [3, 9, 5, 7, 1, 2]
assert graph_2.depth_first(2) == [2, 3, 6, 8, 7, 5, 4]
assert graph_2.depth_first(0) == [0, 3, 6, 8, 7, 5, 4, 2, 1]

#calc_distance
assert graph_3.calc_distance(0,3) == 3
assert graph_3.calc_distance(2,4) == False

#calc_shortest_path
assert graph_3.calc_shortest_path(0,3) == [0, 1, 4, 3]
assert graph_3.calc_shortest_path(3,5) == [3, 1, 4, 5]
assert graph_3.calc_shortest_path(0,5) == [0, 1, 4, 5]
assert graph_3.calc_shortest_path(4,1) == [4, 3, 1]
assert graph_3.calc_shortest_path(2,4) == False
