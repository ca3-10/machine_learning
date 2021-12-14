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
J = Matrix([[7, 7, 8, 3, 2, 0, 6, 0 ,9 ,0 ,7 ,9], [7 ,9 ,4 ,7 ,2 ,9 ,0 ,1 ,5 ,9 ,7 ,3], [6 ,1 ,8 ,0 ,2 ,9 ,0 ,8 ,4 ,6 ,6 ,0], [9 ,9 ,3 ,5 ,6 ,5 ,3 ,4 ,8 ,8 ,7 ,3], [8 ,0 ,5 ,4 ,5 ,6 ,6 ,7 ,5 ,8 ,1, 9], [5 ,7 ,2 ,4 ,3 ,8 ,4 ,7 ,9 ,4 ,0 ,9], [1 ,2 ,7 ,8 ,4 ,1 ,3 ,8 ,8 ,6 ,6 ,8], [7 ,9 ,0 ,5 ,3 ,6 ,0 ,7 ,6 ,6 ,2 ,5], [3 ,8 ,9 ,7 ,9 ,4 ,9 ,6 ,9 ,6 ,2 ,2], [5 ,0 ,2 ,1 ,6 ,4 ,7 ,9 ,1 ,0 ,2 ,3], [0 ,9, 1, 5, 4, 1, 4, 7, 6 ,8 ,4 ,5], [6, 0, 9, 6, 3, 4, 7, 8, 5, 1, 9 ,1]])

# transpose
assert A.transpose().elements == [[1, 3],[2, 4]]
assert B.transpose().elements == [[1, 3, 0], [0, 4, 0], [-2, 5, 1]]
assert C.transpose().elements == [[1, 4], [2, 5], [3, 6]]
assert D.transpose().elements == [[1, 3, 5], [2, 4, 6]]

# add 
A_add = Matrix([[1, 1], [1, 1]])
B_add = Matrix([[1, 1, 1],[0, 1, 3], [1, 1, -2]])

assert (A + A_add).elements == [[2, 3],[4, 5]]
assert (B+B_add).elements == [[2, 1, -1], [3, 5, 8], [1, 1, -1]]

# subtract
C_sub = Matrix([[-1, -2,-3], [1, 1, 1]])
D_sub = Matrix([[-2, -2], [-2, 0], [0, 1]])
assert (C - C_sub).elements == [[2, 4, 6], [3, 4, 5]]
assert (D-D_sub).elements == [[3, 4], [5, 4], [5, 5]]


# scalar_multiply
assert (A * -2).elements and (-2 * A).elements == [[-2, -4],[-6, -8]]
assert (B * 0).elements and (0 * B).elements == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# matrix_multiply
C_multi = Matrix([[2, 2], [2, 2], [1, 0]])
D_multi = Matrix([[1, -1], [0, 0]])
assert (C @ C_multi).elements == [[9, 6], [24, 18]] 
assert (D @ D_multi).elements == [[1, -1], [3, -3], [5, -5]]

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

#rref_determinant
assert A.rref_det() == 2
assert B.rref_det() ==  4
assert C.rref_det() ==  "Cannot take the determinant of a nonsquare matrix"
assert D.rref_det() ==  "Cannot take the determinant of a nonsquare matrix"
assert F.rref_det() == -175

#equality
RE = Matrix([[0,0], [0,0]])
RE1 = Matrix([[0,0],[0,0]])
RE = RE1

#exponentiation
B_expo =  Matrix([[1, 0, -6], [63, 64, 69], [0,0,1]])
(B ** 3).elements == B_expo.elements