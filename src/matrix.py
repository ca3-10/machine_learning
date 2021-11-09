class Matrix:

    def __init__(self, elements): 
        self.elements = elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])
    
    def print(self):
            for i in range(len(self.elements)):
                print(self.elements[i])
    
    def copy(self):
        copy_matrix = [[num for num in row] for row in self.elements]
        return Matrix(copy_matrix)
    
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

    def calc_minor(self, col_index):
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
                minor = self.calc_minor(i)

                #print('i = ', i)
                #print('Coefficient =', coefficent)
                #print('Smaller matrix associated with coefficient above:')
                #minor.print()
                #print()

                cofactor = coefficent_sign * coefficent * minor.calc_determinant()
                det += cofactor
            return det
    
    def find_pivot_row(self, col_index):
        copy_matrix = self.copy()
        for i in range(copy_matrix.num_cols): 
            if copy_matrix.elements[i][col_index] != 0: 
                return i
            if copy_matrix.elements[i][col_index] == 0: 
                return False 
            
    def swap_rows(self, row_1_index, row_2_index):
        copy_matrix = self.copy()
        copy_matrix.elements[row_1_index], copy_matrix.elements[row_2_index] = copy_matrix.elements[row_2_index], copy_matrix.elements[row_1_index]
        return copy_matrix 
    
    def first_nonzero_entry(self, row_index):
        copy_matrix = self.copy() 
        for i in range(copy_matrix.num_cols):
            if copy_matrix.elements[row_index][i] != 0: 
                nonzero = copy_matrix.elements[row_index][i]
                return nonzero

    def leading_entry_equals_one(self,row_index):
        copy_matrix = self.copy()
        divisor = copy_matrix.first_nonzero_entry(row_index)
        for i in range(copy_matrix.num_cols): 
            if divisor == None: 
                return copy_matrix
            copy_matrix.elements[row_index][i] /= divisor
        return copy_matrix
        
    def clear_below(self, row_index):
        copy_matrix = self.copy()
        #print("Initial Matrix:")
        #copy_matrix.print()
        #print()
        row = copy_matrix.elements[row_index]
        for rows in range(row_index + 1,copy_matrix.num_rows):
            subtractor = -(copy_matrix.elements[rows][row_index])
            sub_row = [elements * subtractor for elements in row]
            for i in range(copy_matrix.num_cols):
                #print("rows:", rows)
                #print("i:",i)
                #print("subtractor:", subtractor)
                #print("sub row:", sub_row)
                #print("current colum:" ,i)
                copy_matrix.elements[rows][i] += sub_row[i]
                #copy_matrix.print()
                #print()
        return copy_matrix
    
    def clear_above(self, row_index):
        copy_matrix = self.copy()
        #print("Initial Matrix:")
        #copy_matrix.print()
        #print()
        row = copy_matrix.elements[row_index]
        for rows in copy_matrix.elements[:row_index]:
            subtractor = -rows[row_index]
            sub_row = [elements * subtractor for elements in row] 
            for i in range(copy_matrix.num_cols):
                rows[i] += sub_row[i]
        return copy_matrix

    def rref(self):
        copy_matrix = self.copy()
        row_index = 0 

        for col_index in range(copy_matrix.num_cols):
            if row_index < copy_matrix.num_rows:
                pivot_row = copy_matrix.find_pivot_row(col_index)
                #print("col_index", col_index)
                #print("row_index", row_index)
                #print("pivot_row", pivot_row)
                if pivot_row != row_index: 
                    copy_matrix.swap_rows(pivot_row, row_index)
                copy_matrix = copy_matrix.leading_entry_equals_one(row_index)
                copy_matrix = copy_matrix.clear_below(row_index)
                copy_matrix = copy_matrix.clear_above(row_index)
                #copy_matrix.print()
                #print()
                row_index += 1
        return copy_matrix
        
    def identity(self):
        identity_matrix = []
        for i in range(self.num_rows): 
            identity_matrix.append([])
            for j in range(self.num_cols):
                if i == j: 
                    identity_matrix[i].append(1)
                else: 
                    identity_matrix[i].append(0)
        return Matrix(identity_matrix)

    def augment(self, id_matrix): 
        copy_matrix = self.copy()
        for i in range(copy_matrix.num_rows): 
            for j in range(copy_matrix.num_cols): 
                copy_matrix.elements[i].append(id_matrix.elements[i][j])
        return copy_matrix
    
    def unaugment(self, aug_matrix):
        inverse_matrix = []
        for i in range(self.num_rows): 
            inverse_matrix.append([])
            for j in range(self.num_cols, aug_matrix.num_cols):
                #print("i",i)
                #print("j", j)
                inverse_matrix[i].append(aug_matrix.elements[i][j])
        return Matrix(inverse_matrix)

    def inverse(self): 
        if self.num_rows != self.num_cols: 
            return Matrix([["Only square matrices are invertible"]])
        copy_matrix = self.copy()
        rref_matrix  = copy_matrix.rref()
        identity_matrix = copy_matrix.identity()
        if copy_matrix.calc_determinant == 0:
            return Matrix([["Matrix isn't invertible"]])
        augmented_matrix = copy_matrix.augment(identity_matrix).rref()
        copy_matrix = copy_matrix.unaugment(augmented_matrix) 
        return copy_matrix

    def rref_det(self):
        copy_matrix = self.copy()
        row_index = 0 

        determinant = 1
        if copy_matrix.num_rows != copy_matrix.num_cols: 
            return "Cannot take the determinant of a nonsquare matrix"
        for col_index in range(copy_matrix.num_cols):
            if row_index < copy_matrix.num_rows:
                pivot_row = copy_matrix.find_pivot_row(col_index)
                if pivot_row != row_index: 
                    copy_matrix.swap_rows(pivot_row, row_index)
                    determinant *= 1 
                determinant *= copy_matrix.elements[row_index][col_index]
                copy_matrix = copy_matrix.leading_entry_equals_one(row_index)
                copy_matrix = copy_matrix.clear_below(row_index)
                copy_matrix = copy_matrix.clear_above(row_index)
                #copy_matrix.print()
                #print()
                row_index += 1
        return determinant

