import math 

class KNearestNeighborsClassifier: 

    def __init__(self,k): 
        self.k = k 
    
    def fit(self, data, y):
        self.data = data
        self.y = y
    
    def compute_distances(self, observation): 
    
        distances = [0 for i in range(len(self.data))]
        for rows in self.data: 
            for i in range(len(self.data[0])):
                distances[self.data.index(rows)] += (observation[i]-rows[i]) ** 2
        root_distances = [math.sqrt(x) for x in distances]
        return root_distances
    
    def classify(self, observation):
        distances = self.compute_distances(observation)
        y_copy = self.y

        k_nearest = []
        classifications = []
        for i in range(0,self.k):
            index_min_distance = distances.index(min(distances))

            classifications.append(y_copy[index_min_distance])
            
            distances.pop(index_min_distance)
        
        no_repeating_values  = list(dict.fromkeys(classifications))

        counter = [0 for i in range(len(no_repeating_values))]

        for values in classifications: 
            counter[no_repeating_values.index(values)] += 1

        index_max_value = counter.index(max(counter))
        closest = no_repeating_values[index_max_value]
        return closest
        