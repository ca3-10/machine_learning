
import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from RSS import *

# LINEAR 

def b_one_grad_lin(a, b):
    return ((10 * a) + (6 * b) - 18)

def a_one_grad_lin(a,b): 
    return ((26 * a) + (10 * b) - 42)

line_one = RSS(1, 0, a_one_grad_lin, b_one_grad_lin, learning_rate=0.01, num_interations = 1000000)

assert round(line_one[0], 4) == 1.2857
assert round(line_one[1], 4) == 0.8571

#LINEAR 

def a_two_grad_lin(a, b):
    return (28 * a) + (12 * b) + 2

def b_two_grad_lin(a,b): 
    return (12 * a) + (8 * b) - 4

line_two = RSS(1, 0, a_two_grad_lin, b_two_grad_lin, learning_rate=0.01, num_interations = 1000000)

assert round(line_two[0], 2) == -0.8
assert round(line_two[1], 2) == 1.7

#PARABOLA 

def a_one_grad_pb(a,b,c): 
    return ((196 * a) + (72 * b) + (38 * c) -26)

def b_one_grad_pb(a,b,c): 
    return ((72 * a) + (28 * b) + (12 * c) -10)

def c_one_grad_pb(a,b,c): 
    return ((28 * a) + (12 * b) + (8 * c) - 8)

parobola_1 = RSS_parabola(1,0,0,a_one_grad_pb, b_one_grad_pb, c_one_grad_pb, learning_rate=0.00001, num_interations=1000000)

assert round(parobola_1[0], 2) == -13.08
assert round(parobola_1[1], 2) == 23.59
assert round(parobola_1[2], 2) == 23.59


#PARABOLA
def a_two_grad_pb(a,b,c): 
    return ((196 * a) + (40 * b) + (28 * c) -62)

def b_two_grad_pb(a,b,c): 
    return ((40 * a) + (28 * b) + (1 * c) -1)

def c_two_grad_pb(a,b,c): 
    return ((28 * a) + (4 * b) + (6 * c) - 12)

parobola_2 = RSS_parabola(1,0,0,a_two_grad_pb, b_two_grad_pb, c_two_grad_pb, learning_rate=0.0001, num_interations=1000000)

assert round(parobola_2[0], 4) == 0.5837
assert round(parobola_2[1], 4) == -0.7706
assert round(parobola_2[2], 4) == -0.7702






