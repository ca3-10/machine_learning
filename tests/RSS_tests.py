
import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from RSS import *


def b_one_grad(a, b):
    return ((10 * a) + (6 * b) - 18)

def a_one_grad(a,b): 
    return ((26 * a) + (10 * b) - 42)

rss_one = RSS(1, 0, a_one_grad, b_one_grad, learning_rate=0.01, num_interations = 1000000)

assert round(rss_one[0], 4) == 1.2857
assert round(rss_one[1], 4) == 0.8571

#-------------------


def a_two_grad(a, b):
    return 

def b_two_grad(a,b): 
    return 

rss_two = RSS(1, 0, a_two_grad, b_two_grad, learning_rate=0.01, num_interations = 1000000)



