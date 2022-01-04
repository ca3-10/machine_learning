import sys
sys.path.append('src')
from gradient_descent import *


#single var 

def fprime1(points): 
    x = points[0]
    return x * 2 
minimum1 = minimize([fprime1],[2], 0.1,1000)

assert round(minimum1[0],10) == 0.0

def fprime2(points): 
    x = points[0]
    return (2 * x) + 2
minimum2 = minimize([fprime2],[0], 0.01,10000)

assert round(minimum2[0],2) == -1.0

def fprime3(points):
    x = points[0]
    return (3 * (x ** 2)) + (2 * x)
minimum3 = minimize([fprime3], [-1/2], 0.01, 1000)
minimum3b = minimize([fprime3], [2], 0.01, 1000)

assert round(minimum3[0], 2) == 0.0
assert round(minimum3b[0], 2) == -0.0

#two var

def fx1(points):
    x, y = points[0], points[1] 
    return (2 * x) 

def fy1(points): 
    x, y = points[0], points[1] 
    return(2 * y)


minimum = minimize([fx1,fy1], [10, 10], 0.001, 100000)
assert round(minimum[0], 2) == 0
assert round(minimum[1], 2) == 0

def fx2(points): 
    x, y, z = points[0], points[1], points[2]
    return 2 * (x - 1)
def fy2(points):
    x, y, z = points[0], points[1], points[2]
    return 3 * (y - 1) ** 3
def fz2(points):
    x, y, z = points[0], points[1], points[2]
    return 5 * (z - 1) ** 7

minimum_var_3 = minimize([fx2, fy2, fz2], [1, -2, 2], 0.01, 10000)
assert round(minimum_var_3[0]) == 1 
assert round(minimum_var_3[1]) == 1 
assert round(minimum_var_3[2]) == 1

def fx3(points): 
    return 12 * (points[0] - 90)
def fy3(points):
    return 0.3 * (points[1] + 1)
def fz3(points): 
    return (points[2] - 2) * (points[2] + 2)
def fw3(points):
    return points[3] - 9

minimum_var_4 = minimize([fx3, fy3, fz3, fw3], [10, 5, 6, 9],0.001,100000)
assert round(minimum_var_4[0], 0) == 90
assert round(minimum_var_4[1], 0) == -1
assert round(minimum_var_4[2], 0) == 2
assert round(minimum_var_4[3], 0) == 9
