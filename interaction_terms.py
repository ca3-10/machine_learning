import sys
sys.path.append('src')
from matrix import Matrix

sandwhich = Matrix([(0, 0, 1), (1, 0, 2 ),(2, 0, 4), (4, 0, 8), (6, 0, 9), (0, 2, 2), (0, 4, 5), (0, 6, 7), (0, 8, 6), (2, 2, 1), (3, 4, 1)])
it_sandwhich = Matrix([(1,0, 0, 0), (1, 1, 0, 0),(1, 2, 0, 0), (1, 4, 0, 0), (1, 6, 0, 0), (1, 0, 2, 0), (1, 0, 4, 0), (0, 6, 0), (0, 8, 0), (2, 2, 4), (3, 4, 12)])
rating = Matrix([[1], [2], [4], [8], [9], [2], [5], [7], [6], [1], [1]])

sandwhich_T = sandwhich.transpose()

coeffs = sandwhich_T.matrix_multiply(sandwhich.elements)

ratings = sandwhich_T.matrix_multiply(rating.elements)

coeffs = coeffs.inverse()
coeffs.matrix_multiply(ratings.elements)

[0.0]
[4.441e-16]
[1.0]   

# 5 beef 0 pb 
print(4.441e-16 * 5)

# 5 beef 5 pb
print((4.441e-16 * 5)+(1*5))


