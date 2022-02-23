import math 
import sys
sys.path.append('src')
from matrix import Matrix

class LinearRegressor: 
    
    def fit(self, data, interaction_terms=False): 
        data_matrix = Matrix(data)
        coeffs = []
        y_values_matrix = Matrix([[data_matrix.elements[i][data_matrix.num_cols - 1]] for i in range(0,data_matrix.num_rows)])
    
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

        y_values_matrix = coeff_transpose @ y_values_matrix.elements

        coeff_matrix = coeff_transpose @ coeff_matrix.elements
        coeff_inverse = coeff_matrix.inverse()
        
        constants_values = coeff_inverse @ y_values_matrix
        
        self.coefficents = [constants_values.elements[i][0] for i in range(0, constants_values.num_rows)]
        return self.coefficents
        
        
    
    def predict(self,values, interaction_terms = False): 
        prediction = self.coefficents[0]

        if len(values) != len(self.coefficents) - 1 and interaction_terms == False: 
            return "incorrect number of value entries"
        elif len(values) == 1 and len(self.coefficents)-1 == 1: 
            return self.coefficents[0] + (values[0] * self.coefficents[1])
       
        for i in range(1,self.data_length):
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
            
        return prediction

