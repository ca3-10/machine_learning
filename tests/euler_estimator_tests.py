
import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from euler_estimator import EulerEstimator
import math 

#1 

def derivative_1(point): 
    return point[0]+1

euler_1 = EulerEstimator(derivative_1)
euler_1_estimated = euler_1.calc_estimated_points(point=(1,4), step_size=0.5, num_steps=4)

assert euler_1_estimated[0] == 3.0
assert euler_1_estimated[1] == 9.5

#2-----------

def derivative_2(point): 
    return (point[0] ** 2) * point[1]

euler_2 = EulerEstimator(derivative_2)

euler_2_estimated = euler_2.calc_estimated_points(point=(1,1), step_size=1, num_steps=2)

assert euler_2_estimated[0] == 3
assert euler_2_estimated[1] == 10

#3---------------
#FROM: https://math.libretexts.org/Courses/Monroe_Community_College/MTH_225_Differential_Equations/3%3A_Numerical_Methods/3.1%3A_Euler's_Method

def derivative_3(point): 
    return (-2 * point[1]) + (point[0] ** 3) * (math.exp(-2 * point[0]))

euler_3 = EulerEstimator(derivative_3)

euler_3_estimated = euler_3.calc_estimated_points(point=(0,1), step_size=0.1, num_steps=9)

assert round(euler_3_estimated[0], 1) == 0.9
assert round(euler_3_estimated[1], 2) == 0.16


def_deri


