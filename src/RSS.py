import math 

def RSS_linear(a, b, a_gradient, b_gradient, learning_rate = 0.01, num_interations = 10000):
    a_old = a
    b_old = b 
    for i in range(num_interations):
        a_new = a_old - (learning_rate * a_gradient(a_old, b_old))
        b_new = b_old - (learning_rate * b_gradient(a_old, b_old))
        a_old = a_new
        b_old = b_new

    return (a_new, b_new)

def RSS_parabola(a,b,c,a_gradient,b_gradient, c_gradient, learning_rate, num_interations):
    a_old = a
    b_old = b
    c_old = c
    
    for i in range(num_interations):
        a_new = a_old - learning_rate * a_gradient(a_old, b_old, c_old)
        b_new = b_old - learning_rate * b_gradient(a_old, b_old, c_old)
        c_new = c_old - learning_rate * c_gradient(a_old, b_old, c_old)
        a_old = a_new
        b_old = b_new
        c_old = c_new
    return (a_old, b_old, c_old)    

def RSS_logistic(a, b, a_gradient, b_gradient, learning_rate = 0.01, num_interations = 10000):
    a_old = a
    b_old = b 
    for i in range(num_interations):
        a_new = a_old - (learning_rate * a_gradient(a_old, b_old))
        b_new = b_old - (learning_rate * b_gradient(a_old, b_old))
        a_old = a_new
        b_old = b_new

    return (a_new, b_new)


def a_grad(a, b, c):
    return 2*(a+b+c)+8*(4*a+2*b+c-1)+18*(9*a+3*b+c-1)

def b_grad(a, b, c):
    return 2*(a+b+c)+4*(4*a+2*b+c-1)+6*(9*a+3*b+c-1)

def c_grad(a, b, c):
    return 2*(c-2)+2*(a+b+c)+2*(4*a+2*b+c-1)+2*(9*a+3*b+c-1)

E = RSS_parabola(1, 0, 0, a_grad, b_grad, c_grad, learning_rate=0.0087900003, num_interations=1100)

print(E)