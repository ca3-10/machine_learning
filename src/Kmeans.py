import math

class KMeans: 

    def __init__(self, intitial_clusters, data): 
        self.clusters = intitial_clusters
        self.data = data
    
    def cluster_center_point(self, cluster_key):

        cluster_indicies = self.clusters[cluster_key]
        initial_totals = [0 for i in range(len(self.data[0]))]
        
        for index in cluster_indicies: 
            for i in range(len(self.data[0])):
                initial_totals[i] += self.data[index][i]
        
        cluster_center = []
        for i in range(len(initial_totals)):
            cluster_center.append(initial_totals[i] / len(cluster_indicies))
        
        return cluster_center
    
    def all_centers(self): 
        centers = {key : None for key in self.clusters}
        for key in self.clusters: 
            centers[key] = self.cluster_center_point(key)
        
        self.centers = centers


    def nearest_center(self, point_index): 
        
        point = self.data[point_index]

        distances = { key: 0 for key in self.clusters}
        
        for key in self.clusters: 
            for i in range(len(point)):
                distances[key] += (point[i] - self.centers[key][i]) ** 2
        
        for key in distances: 
            distances[key] = math.sqrt(distances[key])
    
        nearest_center = min(distances, key=distances.get)

        return nearest_center
    
    def reassign(self): 


        new_clusters = {key: [] for key in self.clusters}
        
        indicies = [0 for i in range(len(self.data))]

        for i in range(len(self.data)): 
            indicies[i] += self.nearest_center(i)
        
        for key in new_clusters: 
            for i  in range(len(indicies)): 
                if indicies[i] == key: 
                    new_clusters[key].append(i)
        
        self.clusters = new_clusters
    
    def run(self):
        prev_clusters = {}
        empty_clusters = []
        while prev_clusters != self.clusters:
            prev_clusters = self.clusters
            for cluster_index in list(self.clusters.keys()):
                if len(self.clusters[cluster_index]) == 0:
                    self.clusters.pop(cluster_index)
                    empty_clusters.append(cluster_index)
            self.all_centers()
            self.reassign()
        for index in empty_clusters:
            self.clusters[index] = []

        
