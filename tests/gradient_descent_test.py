import sys
sys.path.append('src')
from gradient_descent import *

def fprime1(x): 
    return x * 2 
minimum1 = minimize(fprime1,2, 0.1,1000)

assert round(minimum1,10) == 0.0

def fprime2(x): 
    return (2 * x) + 2

minimum2 = minimize(fprime2,0, 0.01,10000)

assert round(minimum2,2) == -1.0

def fprime3(x): 
    return (3 * (x ** 2)) + (2 * x)

minimum3 = minimize(fprime3, -1/2, 0.01, 1000)
minimum3b = minimize(fprime3, 2, 0.01, 1000)

assert round(minimum3, 2) == 0.0
assert round(minimum3b, 2) == -0.0
