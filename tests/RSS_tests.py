
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

def a_grad(a, b, c):
    return 2*(a+b+c)+8*(4*a+2*b+c-1)+18*(9*a+3*b+c-1)

def b_grad(a, b, c):
    return 2*(a+b+c)+4*(4*a+2*b+c-1)+6*(9*a+3*b+c-1)

def c_grad(a, b, c):
    return 2*(c-2)+2*(a+b+c)+2*(4*a+2*b+c-1)+2*(9*a+3*b+c-1)


parabola_1 = RSS_parabola(1,0,0,a_grad, b_grad, c_grad,0.00001,1000000)


assert round(parabola_1[0], 2) == 0.5
assert round(parabola_1[1], 2) == -1.7
assert round(parabola_1[2], 2) == 1.8


#PARABOLA
def a_two_grad_pb(a,b,c): 
    return 32 *((16 * a) + (4 * b) + c + 1) + 8 *((4 * a) + (2 * b) + c - 2)

def b_two_grad_pb(a,b,c): 
    return 8*(16 * a + 4 * b + c + 1) + 4*(4 * a + 2 * b + c - 2)

def c_two_grad_pb(a,b,c): 
    return 2*(c+2) + 2*(16 * a + 4 * b + c + 1) + 2*(4 * a + 2 * b + c - 2) + 2 * c

parabola_2 = RSS_parabola(1,0,0,a_two_grad_pb, b_two_grad_pb, c_two_grad_pb, learning_rate=0.001, num_interations=1000000)

assert round(parabola_2[0], 2) == -0.75
assert round(parabola_2[1], 2) == 3
assert round(parabola_2[2], 2) == -1






