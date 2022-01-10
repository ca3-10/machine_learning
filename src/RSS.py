def RSS(a, b, a_gradient, b_gradient, learning_rate = 0.01, num_interations = 10000):
    a_old = a
    b_old = b 
    for i in range(num_interations):
        a_new = a_old - (learning_rate * a_gradient(a_old, b_old))
        b_new = b_old - (learning_rate * b_gradient(a_old, b_old))
        a_old = a_new
        b_old = b_new

    return (a_new, b_new)

def RSS_parabola(a,b,c,a_gradient,b_gradient, c_gradient, learning_rate = 0.01, num_interations = 10000):
    a_old = a
    b_old = b
    c_old = c

    for i in range(num_interations): 
        a_new = a_old - (learning_rate * a_gradient(a_old, b_old, c_old))
        b_new = b_old - (learning_rate * b_gradient(a_old, b_old, c_old))
        c_new = c_old - (learning_rate * c_gradient(a_old, b_old, c_old))

        a_old = a_new
        b_old = b_new
        c_old = b_new
    return (a_new, b_new, c_new)    

def a_grad(a,b,c): 
    return ((196 * a) + (72 * b) + (38 * c) -26)

def b_grad(a,b,c): 
    return ((72 * a) + (28 * b) + (12 * c) -10)

def c_grad(a,b,c): 
    return ((28 * a) + (12 * b) + (8 * c) - 8)


parobola = RSS_parabola(1,0,0,a_grad, b_grad, c_grad, learning_rate=0.00001, num_interations=1000000)
print(parobola)
