import math 


class KMeans: 

    def __init__(self, initial_clusters, data): 
        self.clusters = initial_clusters
        self.data = data 
    
    def cluster_center_point(self, cluster_key):

        cluster_indicies = self.clusters[cluster_key]
        totals = [0 for i in range(len(self.data[0]))]

        for indicies in cluster_indicies: 
            for j in range(len(self.data[0])): 
                totals[j] += self.data[indicies][j]
        
        cluster_center = [totals[i]/len(cluster_indicies) for i in range(len(totals))]

        return cluster_center

    def run(self): 

        initial_centers = {}
        for key in self.clusters: 
            initial_centers[key] = self.cluster_center_point(key)

        distances = {}
        for key in initial_centers: 
            distances[key] = [0 for i in range(len(self.data))]
        
        for key in initial_centers: 
            for i in range(len(self.data)): 
                for j in range(len(self.data[0])):
                    distances[key][i] += (initial_centers[key][j] - self.data[i][j]) ** 2
        
        for key in initial_centers: 
            for i in range(len(initial_centers[key])): 
                distances[key][i] = math.sqrt(distances[key][i])
        
        distances_from_all_centers = [[] for i in range(len(self.data))]
                
            
        
                

data_1 = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]

clusters = {
    1: [0,3,6,9,12,15,18],
    2: [1,4,7,10,13,16],
    3: [2,5,8,11,14,17]
    }

k = KMeans(clusters, data_1)
print(k.run())