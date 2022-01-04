
def minimize(fx,x0,learning_rate=0.001, num_interations = 1000):
    x_old = x0
    y_old = y0
    while num_interations > 0: 
        x_new = x_old - (learning_rate * fx(x_old, y_old))
        x_old = x_new
        num_interations -= 1

    return x_new

def minimize(gradients, initial_points, learning_rate = 0.001, num_interations = 1000): 
    
    for j in range(num_interations):
        for i in range(len(gradients)): 
            initial_points[i] = initial_points[i] - (learning_rate * gradients[i](initial_points)) 
    
    return initial_points


