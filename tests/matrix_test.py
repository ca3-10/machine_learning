import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[1, 2],[3, 4]])
B = Matrix([[1, 0, -2],[3, 4, 5],[0, 0, 1]])
C = Matrix([[1, 2, 3], [4, 5, 6]])
D = Matrix([[1, 2], [3, 4], [5, 6]])



# transpose

assert A.transpose() == [[1, 3],[2, 4]]
assert B.transpose() == [[1, 3, 0], [0, 4, 0], [-2, 5, 1]]
assert C.transpose() == [[1, 4], [2, 5], [3, 6]]
assert D.transpose() == [[1, 3, 5], [2, 4, 6]]

# add 
assert A.add([[1, 1], [1, 1]]) == [[2, 4],[3, 5]]
assert B.add([[1, 1, 1],[1, 1, 1], [1, 1, 1]]) == [[2, 4, 1], [1, 5, 1], [-1, 6, 2]]

# subtract
assert C.subtract([[-1, -2], [-3, 1], [1, 1]]) == [[2, 6], [5, 4], [2, 5]]
assert D.subtract([[-2, -2, -2], [0, 0, 1]]) == [[3, 5, 7], [2, 4, 5]]


# scalar_multiply
assert A.scalar_multiply(-2) == [[-4, -8],[-6, -10]]
assert B.scalar_multiply(0) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# matrix_multiply
assert C.matrix_multiply([[2, 2], [2, 2]]) == [[16, 16], [18, 18], [14, 14]] 
assert D.matrix_multiply([[1, 0, 1], [1, 1, 3], [2, -1, 0]]) == [[22, -2, 18], [16, -1, 14]] 

