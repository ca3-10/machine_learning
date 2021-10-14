import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[1, 2],[3, 4]])
B = Matrix([[1, 0, -2],[3, 4, 5],[0, 0, 1]])
C = Matrix([[1, 2, 3], [4, 5, 6]])
D = Matrix([[1, 2], [3, 4], [5, 6]])
E = Matrix([[1, 2, 3, 4], [0, 1, 0, 2], [1, 1, 0, 4], [3, 0, 2, 1]])
F = Matrix([[1, 2, 3, 4, 5], [1, 1, 2, 0, 0], [-1, -4, 0, 2, 0], [2, 3, 5, 6, 0], [1, 1, 1, 3, 0]])
G = Matrix([[2, 1], [3,2], [-2,1], [1,1]])
H = Matrix([[2, 4, 1, 1], [1, -2, 3, 2], [3, 7, -1, 0], [1, 4, -3, 1]])
I = Matrix([[2, 3, -2],[7, 2, 1],[2, 4, 1],[5, 6, 7]])


# transpose
assert A.transpose().elements == [[1, 3],[2, 4]]
assert B.transpose().elements == [[1, 3, 0], [0, 4, 0], [-2, 5, 1]]
assert C.transpose().elements == [[1, 4], [2, 5], [3, 6]]
assert D.transpose().elements == [[1, 3, 5], [2, 4, 6]]

# add 
assert A.add([[1, 1], [1, 1]]).elements == [[2, 3],[4, 5]]
assert B.add([[1, 1, 1],[0, 1, 3], [1, 1, -2]]).elements == [[2, 1, -1], [3, 5, 8], [1, 1, -1]]

# subtract
assert C.subtract([[-1, -2,-3], [1, 1, 1]]).elements == [[2, 4, 6], [3, 4, 5]]
assert D.subtract([[-2, -2], [-2, 0], [0, 1]]).elements == [[3, 4], [5, 4], [5, 5]]


# scalar_multiply
assert A.scalar_multiply(-2).elements == [[-2, -4],[-6, -8]]
assert B.scalar_multiply(0).elements == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# matrix_multiply
assert C.matrix_multiply([[2, 2], [2, 2], [1, 0]]).elements == [[9, 6], [24, 18]] 
assert D.matrix_multiply([[1, -1], [0, 0]]).elements == [[1, -1], [3, -3], [5, -5]]

#determinant
assert A.calc_determinant() == -2
assert B.calc_determinant() ==  4
assert C.calc_determinant() ==  "not a valid input, matrix must be square"
assert D.calc_determinant() ==  "not a valid input, matrix must be square"
assert E.calc_determinant() == 11
assert F.calc_determinant() == -175

#rref
assert A.rref().elements == [[1, 0], [0, 1]]
assert B.rref().elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert C.rref().elements == [[1, 0, -1], [0, 1, 2]]
assert D.rref().elements == [[1, 0], [0, 1], [0, 0]]
assert E.rref().elements == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
assert F.rref().elements == [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
assert G.rref().elements == [[1, 0], [0, 1], [0, 0], [0, 0]]
assert H.rref().elements == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
assert I.rref().elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]

#inverse 

assert A.inverse().elements == [[-2, 1], [1.5, -0.5]]
assert B.inverse().elements == [[1, 0, 2], [-0.75, 0.25, -2.75], [0, 0, 1]]
assert C.inverse().elements == [["Only square matrices are invertible"]]
assert D.inverse().elements == [["Only square matrices are invertible"]]
