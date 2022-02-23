
import sys
sys.path.append('src')
from matrix import Matrix
from polynomial_regression import PolynomialRegressor


A = PolynomialRegressor()
A.fit([(1, 2), (3, 4), (5, 6)], 2)

assert round(A.coefficents[0], 2) == 1
assert round(A.coefficents[1], 2) == 1
assert round(A.coefficents[2],2) == 0

#--------------------------------------------

B = PolynomialRegressor()
B.fit([(-2.033,0), (-1.5, -0.264), (0,2),(1,6)],3)

assert round(B.coefficents[0],2) == 2
assert round(B.coefficents[1],2) == 3
assert round(B.coefficents[2],2) == 1
assert round(B.coefficents[3],3) ==  0.003

#-------------------------------------------
