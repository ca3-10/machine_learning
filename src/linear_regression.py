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
        
        a_b_values = coeff_inverse.matrix_multiply(y_values_matrix.elements)
        
        self.coefficents = [round(a_b_values.elements[i][0], 5) for i in range(0, a_b_values.num_rows)]
        return self.coefficents
    
    def predict(self,): 
        y = round(self.coefficents[0] + (x_value * self.coefficents[1]), 5)
        return y 
    
A = LinearRegressor()
print(A.fit([(0, 0, 1), (1, 0, 2 ),(2, 0, 4), (4, 0, 8), (6, 0, 9), (0, 2, 2), (0, 4, 5), (0, 6, 7), (0, 8, 6)]))
