import math 
import sys
sys.path.append('src')
from matrix import Matrix


class LogisticRegressor: 
    
    def fit(self, data,interaction_terms = False, M=0, m=0): 
        data_matrix = Matrix(data)
        coeffs = []

        for i in range(data_matrix.num_rows): 
            if data_matrix.elements[i][-1] <= 0: 
                return "y values must be greater than 0 and less than 1"
        
        if M != 0 or m != 0:
            self.max_bound = M
            self.min_bound = m
            y_values_matrix = Matrix([[math.log(((M - data_matrix.elements[i][-1]) / data_matrix.elements[i][-1]) - m)] for i in range(0,data_matrix.num_rows)])
        else:
            y_values_matrix = Matrix([[math.log((1 / data_matrix.elements[i][-1]) - 1)] for i in range(0,data_matrix.num_rows)])
        
        self.data_length = data_matrix.num_cols

        for i in range(data_matrix.num_rows): 
            coeffs.append([1])
            for j in range(0, data_matrix.num_cols - 1):
                coeffs[i].append(data_matrix.elements[i][j])
        

        if interaction_terms == True: 
            og_coeff_len = len(coeffs[0])
            
            for rows in coeffs:
                for m in range(1,og_coeff_len-1):
                    for n in range(1,og_coeff_len-1):
                        if m == m + n or m + n >= self.data_length: 
                            continue
                        rows.append(rows[m]*rows[m+n])
        
        
        coeff_matrix = Matrix(coeffs)
        coeff_transpose = coeff_matrix.transpose()

        y_values_matrix = coeff_transpose.matrix_multiply(y_values_matrix.elements)

        coeff_matrix = coeff_transpose.matrix_multiply(coeff_matrix.elements)
        coeff_inverse = coeff_matrix.inverse()
        
        constants_values = coeff_inverse.matrix_multiply(y_values_matrix.elements)
        self.coefficents = [constants_values.elements[i][0] for i in range(0, constants_values.num_rows)]
        return self.coefficents
    
    def predict(self,values): 

        prediction = self.coefficents[0]
        if len(values) != len(self.coefficents) - 1: 
            return "incorrect number of value entries"
        elif len(values) == 1 and len(self.coefficents)-1 == 1: 
            return 1 / (1 + math.exp(self.coefficents[0] + (values[0] * self.coefficents[1])))
        
        for i in range(1,len(self.coefficents)):
            prediction += self.coefficents[i] * values[i -1]
        
        if interaction_terms == True: 
            original_values_length = len(values)
            interaction_values = []
            interaction_coeffs = self.coefficents[self.data_length:]
            
            for i in range(0, original_values_length ):
                for j in range(0, original_values_length):
                    if i == i + j or i + j >= len(values): 
                            continue
                    interaction_values.append(values[i]*values[i+j])
            
            for i in range(0, len(interaction_values)):
                prediction += (interaction_values[i] * interaction_coeffs[i])

        if self.min_bound != 0 or self.max_bound != 0:
            return self.min_bound + ((self.max_bound - self.min_bound)/(1 + math.exp(prediction)))
        return (1 / (1 + math.exp(prediction)))
    
