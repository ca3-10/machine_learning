import sys
sys.path.append('src')
from matrix import Matrix
from linear_regression import LinearRegressor

A = LinearRegressor()
B = LinearRegressor()
C = LinearRegressor()
D = LinearRegressor()
E = LinearRegressor()
F = LinearRegressor()
G = LinearRegressor()

#fit 
assert A.fit([(1, 0.2), (2, 0.25), (3, 0.5)]) == [0.01667, 0.15]
assert B.fit([(0.5, -2), (0, 0.7), (6, 0.5)]) == [-0.63158, 0.16842]
assert C.fit([(2, 0.3), (6, 0.2), (-5, 0.45)]) == [0.33925, -0.02258]
assert D.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6]]) == [0.6, 1.8, 0.675]
assert E.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6], [0, 6, 7]]) == [0.82031, 1.72656, 0.78516]
assert F.fit([[1, 2, 3, 4], [2, -2, 1, 0], [6, 2, 1, 3], [0, 1, 2, 1], [-1, -4, 5, 7]], True) == [-56.0, 72.0, 24.0, 6.0, -17.0, -30.0, 1.0625]
assert G.fit([[1, 2, 3, 1, 5, -6], [8, 1, -2, 4, -3,7], [0, 8, 1,-1, 3, 4]], True) == [-20736.0, -87.75, -1120.0, -736.0, -12928.0, -7168.0, -5824.0, 2304.0, 3680.0,1600.0, 5376.0, -2336.0, -2144.0, -23936.0, 8512.0, 636.0]

#predict
assert A.predict([4]) == 0.61667
assert B.predict([4]) == 0.0421
assert C.predict([4]) == 0.24893
assert D.predict([1, 1]) == 3.075
assert E.predict([1, -2]) == 0.97655
assert F.predict([1, 1,1], True) == 0.0625
assert G.predict([1,2,-1,1,1], True) == -54747.74 
