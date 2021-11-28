

class DataFrame: 

    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.column_order = column_order
    
    def to_array(self):
        array = [[] for i in range(len(self.data_dict[self.column_order[0]])) ]
        for values in self.column_order: 
            for i in range(len(array)): 
                array[i].append(self.data_dict[values][i])
        return array
    
    def select_columns(self, columns): 
        


           
    
    #def select_columns(self,selected_columns):
        

    
data_dict = {"Pete": [1, 0, 1, 0],"John": [2, 1, 0, 2],"Sarah": [3, 1, 4, 0]}
df1 = DataFrame(data_dict, column_order = ["John","Pete", "Sarah"])
print(df1.to_array())
