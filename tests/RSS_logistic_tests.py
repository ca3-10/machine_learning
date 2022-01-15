
import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from RSS import *



#LOGISTIC 

def a_one_grad_lg(a,b):
     return (-2 * (((1 + math.exp(a+ b)) ** -1) - 0.5)*((1 + math.exp(a+b)) ** -2)*(math.exp(a+b))
-8 * (((1 + math.exp(4 * a + b)) ** -1) - 1)*((1 + math.exp(4*a+b)) ** -2)*(math.exp(4*a+b)))

def b_one_grad_lg(a,b):
    return ( -2 * ((1+math.exp(b)) ** -1)*((1+math.exp(b))** -2 )*(math.exp(b))
-2 * (((1 + math.exp(a+ b)) ** -1) - 0.5)*((1 + math.exp(a+b)) ** -2)*(math.exp(a+b))
-2 * (((1 + math.exp(4 * a + b)) ** -1) - 1)*((1 + math.exp(4*a+b)) ** -2)*(math.exp(4*a+b)))


logistic_one = RSS_logistic(-1, 0, a_one_grad_lg, b_one_grad_lg,0.01,10000000)

assert round(logistic_one[0],1) == -6.1
assert round(logistic_one[1],1) == 6.1

def a_two_grad_lg(a,b):
     return (-3 * (((1 + math.exp(1.5*a+ b)) ** -0.8) - 1)*((1 + math.exp(1.5*a+b)) ** -2)*(math.exp(1.5*a+b))
-2 * (((1 + math.exp(a + b)) ** -1) - 1)*((1 + math.exp(a+b)) ** -2)*(math.exp(5*a+b)))

def b_two_grad_lg(a,b):
    return ( -2 * ((1+math.exp(b)) ** -1)*((1+math.exp(b))** -2 )*(math.exp(b))
-2 * (((1 + math.exp(1.5*a+ b)) ** -1) - 0.8)*((1 + math.exp(1.5*a+b)) ** -2)*(math.exp(1.5*a+b))
-2 * (((1 + math.exp(a + b)) ** -1) - 1)*((1 + math.exp(a+b)) ** -2)*(math.exp(a+b)))

logistic_two = RSS_logistic(-1, 0, a_two_grad_lg, b_two_grad_lg,0.01,1000000)

assert round(logistic_two[0],2) == -5.45
assert round(logistic_two[1],2) ==  2.79
