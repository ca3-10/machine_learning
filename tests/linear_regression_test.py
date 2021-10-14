import sys
sys.path.append('src')
from matrix import Matrix
from linear_regression import LinearRegressor

A = LinearRegressor()
B = LinearRegressor()
C = LinearRegressor()


#fit 
assert A.fit([(1, 0.2), (2, 0.25), (3, 0.5)]) == [0.01667, 0.15]
assert B.fit([(0.5, -2), (0, 0.7), (6, 0.5)]) == [-0.63158, 0.16842]
assert C.fit([(2, 0.3), (6, 0.2), (-5, 0.45)]) == [0.33925, -0.02258]

#predict
assert A.predict(4) == 0.61667
assert B.predict(4) == 0.0421
assert C.predict(4) == 0.24893
