

class DataFrame: 

    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.column_order = column_order
    
    def select_columns(self, columns): 
        copy_dict = {}
        for col_values in columns: 
            copy_dict[col_values] = self.data_dict[col_values]
        return DataFrame(copy_dict, column_order = columns)
    
    def select_rows(self, rows): 
        selected_rows = []
        array = self.to_array()
        for row in rows: 
            selected_rows.append(array[row])
        
        return DataFrame(selected_rows, self.column_order)

    def to_array(self):
        array = [[] for i in range(len(self.data_dict[self.column_order[0]]))]
        for values in self.column_order: 
            for i in range(len(array)):
                array[i].append(self.data_dict[values][i])
        return array 

    def to_json(self): 
        arr_of_dicts = [{} for i in range(len(self.data_dict)+1)]
        for i in range(len(arr_of_dicts)): 
            for values in self.column_order:
                arr_of_dicts[i][values] = self.data_dict[values][i]
        return arr_of_dicts
   
    @classmethod
    def from_array(cls, arr, column_order):
        dict = {}
        for values in column_order:
            dict[values] = []
            for j in range(len(arr)):
                dict[values].append(arr[j][column_order.index(values)])
        return cls(dict, column_order = column_order)
    
    @classmethod
    def from_json(cls,json, column_order):
        dict = {}
        for values in column_order: 
            dict[values] = []
            for i in range(0, len(json)-1):
                dict[values].append(json[i][values])
        return cls(dict, column_order = column_order)

    def order_by(self, order_var, ascending = True):
        order_var_index = self.column_order.index(order_var)
        if ascending == True: 
            sorted = self.simple_sort_min(order_var_index)
            return DataFrame.from_array(sorted, self.column_order)
        elif ascending == False: 
            sorteds = self.simple_sort_max(order_var_index)
            return DataFrame.from_array(sorteds, self.column_order)

    def calc_min_index(self,unsorted, index):
        minimum = unsorted[0]
        for num in unsorted:
            if num[index] < minimum[index]:
                minimum = num
        return minimum
    
    def calc_max_index(self,unsorted, index):
        maximum = unsorted[0]
        for num in unsorted:
            if num[index] > maximum[index]:
                maximum = num
        return maximum
    
    def simple_sort_min(self,index):
        sorted_list = []
        arr = self.to_array()
        while len(arr) > 0:
            miniMum = self.calc_min_index(arr,index)
            sorted_list.append(miniMum)
            arr.remove(miniMum)
        return sorted_list
    
    def simple_sort_max(self,index):
        sorted_list = []
        arr = self.to_array()
        while len(arr) > 0:
            maxiMum = self.calc_max_index(arr, index)
            sorted_list.append(maxiMum)
            arr.remove(maxiMum)
        return sorted_list


    
data_dict = {"Pete": [1, 0, 1, 0],"John": [2, 1, 0, 2],"Sarah": [3, 1, 4, 0]}
df1 = DataFrame(data_dict,["John","Sarah", "Pete"])
#print(df1.to_array())
df2 = df1.select_columns(["Sarah", "Pete"])
df3 = df1.select_rows([1,3])

columns = ['firstname', 'lastname', 'age']
arr = [['Kevin', 'Fray', 5], ['Charles', 'Trapp', 17], ['Anna', 'Smith', 13], ['Sylvia', 'Mendez', 9]]

df = DataFrame.from_array(arr, columns)
gh = df.order_by("firstname", ascending = False).to_array()
print(gh)
