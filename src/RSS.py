def RSS(a, b, a_gradient, b_gradient, learning_rate = 0.01, num_interations = 10000):
    a_old = a
    b_old = b 
    for i in range(num_interations):
        a_new = a_old - (learning_rate * a_gradient(a_old, b_old))
        b_new = b_old - (learning_rate * b_gradient(a_old, b_old))
        a_old = a_new
        b_old = b_new

    return (a_new, b_new)
