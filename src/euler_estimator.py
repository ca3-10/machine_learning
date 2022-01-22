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



def da_dt(t, state):
    return state["a"] + 1

def db_dt(t, state):
    return state["a"] + state["b"]

def dc_dt(t, state):
    return 2 * state["b"] + 3 * t

derivatives_1 = {"a": da_dt, "b": db_dt, "c": dc_dt}

initial_state = {"a": -0.45, "b": -0.05, "c": 0}
initial_point = (-0.4, initial_state)

D = EulerEstimator(derivatives_1)
F=D.calc_estimated_points(initial_point, step_size=2, num_steps=4)
print(F)
