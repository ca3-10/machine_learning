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
        if len(self.coefficents) == 2: 
            prediction += self.coefficents[0] + self.coefficents[1] * x_value
            return prediction
        for i in range(0,len(self.coefficents)-1):
            print(i)
            prediction += self.coefficents[i] * ((x_value)**(i))
        return prediction


data_points = [(1,3), (2,10), (3,40), (4,25), (5,90), (6,100), (7,180), (8,140), (9,250), (10,260)]

#linear
lin = PolynomialRegressor()
lin.fit(data_points, 1)
print(len(lin.coefficents))
print(lin.predict(4))