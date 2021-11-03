import math 
import sys
sys.path.append('src')
from matrix import Matrix

class LinearRegressor: 
    
    def fit(self, data): 
        data_matrix = Matrix(data)
        coeffs = []
        
        y_values_matrix = Matrix([[data_matrix.elements[i][data_matrix.num_cols - 1]] for i in range(0,data_matrix.num_rows)])
        
        for i in range(data_matrix.num_rows): 
            coeffs.append([1])
            for j in range(0, data_matrix.num_cols - 1):
                coeffs[i].append(data_matrix.elements[i][j])
        
        coeff_matrix = Matrix(coeffs)

        coeff_transpose = coeff_matrix.transpose()

        y_values_matrix = coeff_transpose.matrix_multiply(y_values_matrix.elements)

        coeff_matrix = coeff_transpose.matrix_multiply(coeff_matrix.elements)
        coeff_inverse = coeff_matrix.inverse()
        
        constants_values = coeff_inverse.matrix_multiply(y_values_matrix.elements)
        
        self.coefficents = [round(constants_values.elements[i][0], 5) for i in range(0, constants_values.num_rows)]
        return self.coefficents
    
    def predict(self,values): 
        prediction = self.coefficents[0]
        if len(values) != len(self.coefficents) - 1: 
            return "incorrect number of value entries"
        elif len(values) == 1 and len(self.coefficents)-1 == 1: 
            return round(self.coefficents[0] + (values[0] * self.coefficents[1]), 5)
        for i in range(1,len(self.coefficents)):
            prediction += self.coefficents[i] * values[i -1]
        return round(prediction, 5)
