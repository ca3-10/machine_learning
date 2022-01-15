
import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from RSS import *


def b_one_grad_lin(a, b):
    return ((10 * a) + (6 * b) - 18)

def a_one_grad_lin(a,b): 
    return ((26 * a) + (10 * b) - 42)

line_one = RSS_linear(1, 0, a_one_grad_lin, b_one_grad_lin, learning_rate=0.01, num_interations = 1000000)

assert round(line_one[0], 4) == 1.2857
assert round(line_one[1], 4) == 0.8571


def a_two_grad_lin(a, b):
    return (28 * a) + (12 * b) + 2

def b_two_grad_lin(a,b): 
    return (12 * a) + (8 * b) - 4

line_two = RSS_linear(1, 0, a_two_grad_lin, b_two_grad_lin, learning_rate=0.01, num_interations = 1000000)

assert round(line_two[0], 2) == -0.8
assert round(line_two[1], 2) == 1.7