import sys
sys.path.append('src')
from matrix import Matrix
from logistic_regression import LogisticRegressor

A = LogisticRegressor()
B = LogisticRegressor()
C = LogisticRegressor()
D = LogisticRegressor()
E = LogisticRegressor()

A.fit([(1, 0.2), (2, 0.25), (3, 0.5)])
B.fit([(0.5, -2), (0, 0.7), (6, 0.5)])
C.fit([[9, 0, 0.1], [1, 0, 0.2], [2, 0, 0.4], [4, 0, 0.8], [0, 8, 0.6]])
D.fit([[11, 22, 0.3], [17, 1, 0.6], [0, 10, 0.2]])


#coefficents
assert round(A.coefficents[0], 5) == 2.2146 and round(A.coefficents[1], 5) == -0.69315
assert B.fit([(0.5, -2), (0, 0.7), (6, 0.5)]) == "y values must be greater than 0 and less than 1"
assert round(C.coefficents[0], 5) == 0.01738
assert round(C.coefficents[1], 5) == 0.15832
assert round(C.coefficents[2], 5) == -0.05286
assert round(D.coefficents[0], 5) == 1.03823
assert round(D.coefficents[1], 5) == -0.08697
assert round(D.coefficents[2], 5) == 0.03481

#predict

assert round(A.predict([4]), 5) == 0.63599
assert round(C.predict([2, 1]), 5) == 0.43017
assert round(D.predict([0.5, 3]), 4) == 0.2499

# generalized bounds and interation terms 

logistic_regressor = LogisticRegressor()
test_data = [[0, 0, 1], [2, 2, 1], [6, 0, 9], [0, 6, 7]]

logistic_regressor.fit(test_data,True,10,0)
coefficients = logistic_regressor.coefficents

assert round(coefficients[0], 3) == 2.197 and round(coefficients[1], 3) == -0.732 and round(coefficients[2], 3) == -0.507 and round(coefficients[3], 3) == 0.620
assert logistic_regressor.predict([5,5], True) < 1
assert round(logistic_regressor.predict([0,6], True)) == 7 

