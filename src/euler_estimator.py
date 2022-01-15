import math 

class EulerEstimator: 

    def __init__(self, derivative): 
        self.derivative = derivative
    
    def calc_derivative_at_point(self, point):
        return self.derivative(point)

    def calc_estimated_points(self, point, step_size, num_steps):
        point = list(point)
        for i in range(num_steps): 
            slope = self.derivative(point)
            point[1] = point[1] + step_size * slope 
            point[0] = point[0] + step_size
        return (point[0], point[1])



