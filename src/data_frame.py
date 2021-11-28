

class DataFrame: 

    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.column_order = column_order
    
    def to_array(self):
        array = [[] for i in range(len(self.data_dict[self.column_order[0]]))]
        for values in self.column_order: 
            for i in range(len(array)): 
                array[i].append(self.data_dict[values][i])
        return array 
    
    def select_columns(self, columns): 
        copy_dict = {}
        for col_values in columns: 
            copy_dict[col_values] = self.data_dict[col_values]
        return DataFrame(copy_dict, column_order = columns)
    
    def select_rows(self, rows): 
        
    

        

        

    
data_dict = {"Pete": [1, 0, 1, 0],"John": [2, 1, 0, 2],"Sarah": [3, 1, 4, 0]}
df1 = DataFrame(data_dict,["John","Pete", "Sarah"])
#print(df1.to_array())
df2 = df1.select_columns(["Sarah", "Pete"])
print(df2.to_array())
print(df1.to_array())