class Matrix:
    def __init__(self, element): 
        self.elements = element
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
        #self.elements = transposed
        return Matrix(transposed)
    
    def add(self, add_matrix):
        added_matrix = []
        for i in range(self.num_rows):
            added_matrix.append([])
            for j in range(self.num_cols):
                added_matrix[i].append(self.elements[i][j] + add_matrix[i][j])
        #self.elements = added_matrix 
        return Matrix(added_matrix)

    def subtract(self, sub_matrix):
        subtracted_matrix = []
        for i in range(self.num_rows):
            subtracted_matrix.append([])
            for j in range(self.num_cols):
                subtracted_matrix[i].append(self.elements[i][j] - sub_matrix[i][j])
        #self.elements = added_matrix 
        return Matrix(subtracted_matrix)

    def scalar_multiply(self,scalar):
        scaled_matrix = []
        for i in range(self.num_rows):
            scaled_matrix.append([])
            for j in range(self.num_cols):
                scaled_matrix[i].append(self.elements[i][j] * scalar)
        #self.elements = added_matrix 
        return Matrix(scaled_matrix)

    def matrix_multiply(self,times_matrix):
        multi_matrix = [[] for in range(self.num_rows)]
        for i in range(self.num_rows):
            multi_matrix.append([])
            for j in range(len(times_matrix[0])):
                multi_matrix[i].append(0)
                for k in range(len(times_matrix)):
                    multi_matrix[i][j] += (self.elements[i][k] * times_matrix[k][j])
        return Matrix(multi_matrix)



