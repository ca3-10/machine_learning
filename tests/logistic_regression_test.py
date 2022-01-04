import sys
sys.path.append('src')
from matrix import Matrix
from logistic_regression import LogisticRegressor

A = LogisticRegressor()
B = LogisticRegressor()
C = LogisticRegressor()
D = LogisticRegressor()
E = LogisticRegressor()

print(E.fit([(0, 0.1), (0, 0.1), (0, 0.1)]))

#fit 
assert A.fit([(1, 0.2), (2, 0.25), (3, 0.5)]) == [2.2146, -0.69315]
assert B.fit([(0.5, -2), (0, 0.7), (6, 0.5)]) == "y values must be greater than 0 and less than 1"
assert C.fit([[9, 0, 0.1], [1, 0, 0.2], [2, 0, 0.4], [4, 0, 0.8], [0, 8, 0.6]]) == [0.01738, 0.15832, -0.05286]
assert D.fit([[11, 22, 0.3], [17, 1, 0.6], [0, 10, 0.2]]) == [1.03823, -0.08697, 0.03481]
#predict

assert A.predict([4]) == 0.63599
assert C.predict([2, 1]) == 0.43017
assert D.predict([0.5, 3]) == 0.24989
