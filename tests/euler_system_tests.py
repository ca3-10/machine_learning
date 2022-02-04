
import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from euler_estimator import EulerEstimator
import math 

def da_dt(t, state):
    return state["a"] + 1

def db_dt(t, state):
    return state["a"] + state["b"]

def dc_dt(t, state):
    return 2 * state["b"] + 3 * t

derivatives_1 = {"a": da_dt, "b": db_dt, "c": dc_dt}

initial_state = {"a": -0.45, "b": -0.05, "c": 0}
initial_point = (-0.4, initial_state)

D = EulerEstimator(derivatives_1)
F = D.calc_estimated_points(initial_point, step_size=2, num_steps=3)
for i in range(0,10): 
    print(D.calc_estimated_points(initial_point, step_size=2, num_steps=i))

assert F[0] == 5.6
assert round(F[1]['a'], 4) == 13.85 
assert round(F[1]['b'], 4) == 2.35 
assert round(F[1]['c'], 4) == 17.00