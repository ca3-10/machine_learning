import sys
sys.path.append('src')
from linear_regression import LinearRegressor

A = LinearRegressor()
A.fit([(0, 0, 1), (1, 0, 2 ),(2, 0, 4), (4, 0, 8), (6, 0, 9), (0, 2, 2), (0, 4, 5), (0, 6, 7), (0, 8, 6)])
