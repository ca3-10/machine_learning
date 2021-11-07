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
        
        og_coeff_len = len(coeffs[0])
        for rows in coeffs:
            for m in range(1,og_coeff_len-1):
                for n in range(1,og_coeff_len-1):
                    if m == m + n or m + n >= 5: 
                        continue
                    rows.append(rows[m]*rows[m+n])
        
        coeff_matrix = Matrix(coeffs)
        coeff_matrix.print()

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


A = LinearRegressor()
print(A.fit([(0, 0, 1), (1, 0, 2 ),(2, 0, 4), (4, 0, 8), (6, 0, 9), (0, 2, 2), (0, 4, 5), (0, 6, 7), (0, 8, 6), (2, 2, 1), (3, 4, 1)]))
