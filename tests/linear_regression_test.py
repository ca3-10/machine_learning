import sys
sys.path.append('src')
from matrix import Matrix
from linear_regression import LinearRegressor

A = LinearRegressor()
B = LinearRegressor()
C = LinearRegressor()
D = LinearRegressor()
E = LinearRegressor()


#fit 
assert A.fit([(1, 0.2), (2, 0.25), (3, 0.5)]) == [0.01667, 0.15]
assert B.fit([(0.5, -2), (0, 0.7), (6, 0.5)]) == [-0.63158, 0.16842]
assert C.fit([(2, 0.3), (6, 0.2), (-5, 0.45)]) == [0.33925, -0.02258]
assert D.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6]]) == [0.6, 1.8, 0.675]
assert E.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6], [0, 6, 7]]) == [0.82031, 1.72656, 0.78516]


#predict
assert A.predict([4]) == 0.61667
assert B.predict([4]) == 0.0421
assert C.predict([4]) == 0.24893
assert D.predict([1, 1]) == 3.075
assert E.predict([1, -2]) == 0.97655
