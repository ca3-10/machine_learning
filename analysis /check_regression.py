import sys
sys.path.append('src')
from matrix import Matrix


#linear_regression 
A = Matrix([[1, 1], [1, 2], [1, 3]])
Y = Matrix([[0.2], [0.25], [0.5]])
A.check_regression(Y.elements).print()
print()

#logistic_regression
B = Matrix([[1, 1], [2, 1], [3, 1]])
Z = Matrix([[1.38629436112], [1.09861228867], [0]])
B.check_regression(Z.elements).print()