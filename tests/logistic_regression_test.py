import sys
sys.path.append('src')
from matrix import Matrix
from logistic_regression import LogisticRegressor

A = LogisticRegressor()
B = LogisticRegressor()
C = LogisticRegressor()

#fit 
assert A.fit([(1, 0.2), (2, 0.25), (3, 0.5)]) == [2.2146, -0.69315]
assert B.fit([(0.5, -2), (0, 0.7), (6, 0.5)]) == "y values must be greater than 0 and less than 1"
assert C.fit([(2, 0.3), (6, 0.2), (-5, 0.45)]) == [0.70538, 0.10604]


#predict
assert A.predict(4) == 0.63599
assert C.predict(4) == 0.24425