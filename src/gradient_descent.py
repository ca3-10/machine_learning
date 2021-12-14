
def minimize(fprime, x0, learning_rate=0.001, num_interations = 1000):
    x_old = x0
    while num_interations > 0: 
        x_new = x_old - (learning_rate * fprime(x_old))
        x_old = x_new
        num_interations -= 1
    return x_new
