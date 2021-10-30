import math 
import sys
sys.path.append('src')
from matrix import Matrix


class LogisticRegressor: 
    
    def fit(self, data): 
        data_matrix = Matrix(data)
        coeffs = []

        for i in range(data_matrix.num_rows): 
            if data_matrix.elements[i][1] <= 0: 
                return "y values must be greater than 0 and less than 1"
                
        y_values_matrix = Matrix([[math.log((1 / data_matrix.elements[i][data_matrix.num_cols]) - 1)] for i in range(0,data_matrix.num_rows)])
        
        for i in range(data_matrix.num_rows): 
            coeffs.append([1])
            for j in range(0, data_matrix.num_cols - 1):
                coeffs[i].append(data_matrix.elements[i][j])
        
        coeff_matrix = Matrix(coeffs)
        coeff_transpose = coeff_matrix.transpose()

        y_values_matrix = coeff_transpose.matrix_multiply(y_values_matrix.elements)

        coeff_matrix = coeff_transpose.matrix_multiply(coeff_matrix.elements)
        coeff_inverse = coeff_matrix.inverse()
        
        a_b_values = coeff_inverse.matrix_multiply(y_values_matrix.elements)
        self.coefficents = [round(a_b_values.elements[i][0], 5) for i in range(0, a_b_values.num_rows)]
        return self.coefficents
    
    def predict(self, x_value): 
        y = round(1 / (1 + math.exp(self.coefficents[0] + (x_value * self.coefficents[1]))), 5)
        return y
    
    
A = LogisticRegressor()
print(A.fit([(0, 0, 1), (1, 0, 2 ),(2, 0, 4), (4, 0, 8), (6, 0, 9), (0, 2, 2), (0, 4, 5), (0, 6, 7), (0, 8, 6)]))
