class Matrix:

    def __init__(self, elements): 
        self.elements = elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])
    
    def print(self):
            for i in range(len(self.elements)):
                print(self.elements[i])
    
    def transpose(self):
        transposed = []
        for i in range(self.num_cols):
            transposed.append([])
            for j in range(self.num_rows):
                transposed[i].append(self.elements[j][i])
        return Matrix(transposed)
    
    def add(self, add_matrix):
        added_matrix = []
        for i in range(self.num_rows):
            added_matrix.append([])
            for j in range(self.num_cols):
                added_matrix[i].append(self.elements[i][j] + add_matrix[i][j])
        return Matrix(added_matrix)

    def subtract(self, sub_matrix):
        subtracted_matrix = []
        for i in range(self.num_rows):
            subtracted_matrix.append([])
            for j in range(self.num_cols):
                subtracted_matrix[i].append(self.elements[i][j] - sub_matrix[i][j])
        return Matrix(subtracted_matrix)

    def scalar_multiply(self,scalar):
        scaled_matrix = []
        for i in range(self.num_rows):
            scaled_matrix.append([])
            for j in range(self.num_cols):
                scaled_matrix[i].append(self.elements[i][j] * scalar)
        return Matrix(scaled_matrix)

    def matrix_multiply(self,times_matrix):
        multi_matrix = []
        for i in range(self.num_rows):
            multi_matrix.append([])
            for j in range(len(times_matrix[0])):
                multi_matrix[i].append(0)
                for k in range(len(times_matrix)):
                    multi_matrix[i][j] += (self.elements[i][k] * times_matrix[k][j])
        return Matrix(multi_matrix)

    def copy(self):
        copy_matrix = [[num for num in row] for row in self.elements]
        return Matrix(copy_matrix)

    def minor_calc(self, col_index):
        minor_matrix = self.copy()
        for i in range(1,minor_matrix.num_cols):
            # print("element to be removed:", minor_matrix.elements[i][col_index])
            minor_matrix.elements[i].pop(col_index)
            #print("row =", i)
            #print("column =", col_index)
            #minor_matrix.print()
            #print()
        minor_matrix.elements.remove(minor_matrix.elements[0])
        return minor_matrix
        
    def calc_determinant(self): 
        #print('Calling calc_determinant on the following matrix:')
        #self.print()
        #print()

        copy_matrix = self.copy()

        if copy_matrix.num_rows != copy_matrix.num_cols: 
            return "not a valid input, matrix must be square"
            
        elif copy_matrix.num_rows == 2 and copy_matrix.num_cols == 2: 
            determinant = (copy_matrix.elements[0][0] * copy_matrix.elements[1][1]) - (copy_matrix.elements[0][1] * copy_matrix.elements[1][0])
            return determinant

        else: 
            det = 0 
            for i in range(copy_matrix.num_cols):
                coefficent_sign = (-1) ** i
                coefficent = self.elements[0][i]
                minor = self.minor_calc(i)

                #print('i = ', i)
                #print('Coefficient =', coefficent)
                #print('Smaller matrix associated with coefficient above:')
                #minor.print()
                #print()

                cofactor = coefficent_sign * coefficent * minor.calc_determinant()
                det += cofactor
            return det

