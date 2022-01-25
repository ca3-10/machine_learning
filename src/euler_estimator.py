import math 

class EulerEstimator: 

    def __init__(self, derivatives): 
        self.derivatives = derivatives
    
    def calc_derivative_at_point(self, point):
        t = point[0]
        states = point[1]
        updated_states = {}
        for key in self.derivatives:
            updated_states[key] = self.derivatives[key](t, states)

        return updated_states


    def calc_estimated_points(self, point, step_size, num_steps):
        
        t = point[0]
        states = point[1]
        updated_states = {}
        og_point = point

        for i in range(num_steps):
            for key in point[1]:
                slopes = self.calc_derivative_at_point(og_point)
                updated_states[key] = states[key] + step_size * slopes[key]
            
            t += step_size
            states = updated_states
            updated_states = {}
            og_point = [t, states]
            
        return og_point


