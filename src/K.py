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
        for i in range(self.k):
            index_min_distance = distances.index(min(distances))

            #k_nearest.append(distances[index_min_distance])
            classifications.append(y_copy[index_min_distance])

            distances.pop(index_min_distance)
            y_copy.pop(index_min_distance)

        no_repeating_values  = list(dict.fromkeys(classifications))
        counter = [0 for i in range(len(no_repeating_values))]

        for values in classifications: 
            counter[no_repeating_values.index(values)] += 1 
        
        index_max_value = counter.index(max(counter))
        closest = no_repeating_values[index_max_value]

        return closest
        


        
knn = KNearestNeighborsClassifier(5)
x = [[0.14,0.14,0.28,0.44],[0.10,0.18,0.28,0.44],[0.12,0.10,0.33,0.45],[0.10,0.25,0.25,0.40],[0.00,0.10,0.40,0.50],[0.00,0.20,0.40,0.40],[0.10,0.08,0.35,0.47],[0.00,0.05,0.30,0.65],[0.20,0.00,0.40,0.40],[0.25,0.10,0.30,0.35],[0.22,0.15,0.50 ,0.13],[0.15,0.20,0.35,0.30],[0.22,0.00 ,0.40,0.38]]
y = ["Shortbread", "Shortbread", "Shortbread", "Shortbread", "Sugar", "Sugar", "Sugar", "Sugar", "Fortune", "Fortune", "Fortune", "Fortune", "Fortune"]                
knn.fit(x, y)
#print(knn.compute_distances([0.10,0.15,0.30,0.45]))
knn.classify([0.10, 0.15, 0.30, 0.45])