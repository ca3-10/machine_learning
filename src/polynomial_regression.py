import math 
import sys
sys.path.append('src')
from matrix import Matrix


class PolynomialRegressor: 

    def fit(self,data, nth_degree): 
        
        y_values = [[row[-1]] for row in data]
        y_matrix = Matrix(y_values)

        coeff = [[1] for i in range(len(data))]
        for i in range(len(data)): 
            for j in range(1, nth_degree + 1):
                coeff[i].append((data[i][0]) ** j)
        
        coeff_matrix = Matrix(coeff)
        coeff_transpose = coeff_matrix.transpose()
        inverse_transpose_coeff = coeff_transpose @ coeff_matrix
        inverse_transpose_coeff = inverse_transpose_coeff.inverse()
        
        y_matrix = coeff_transpose @ y_matrix 
        y_matrix = inverse_transpose_coeff @ y_matrix

        self.coefficents = [y_matrix.elements[i][0] for i in range(0, y_matrix.num_rows)]
        return self.coefficents
    
    def predict(self, x_value): 
        prediction = 0
        for i in range(0,len(self.coefficents)):
            prediction += self.coefficents[i] * ((x_value)**(i))
        return prediction


