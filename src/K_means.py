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
        #sum
        for key in initial_centers: 
            for i in range(len(self.data)): 
                for j in range(len(self.data[0])):
                    distances[key][i] += (initial_centers[key][j] - self.data[i][j]) ** 2
        #distances
        for key in initial_centers: 
            for i in range(len(initial_centers[key])): 
                distances[key][i] = math.sqrt(distances[key][i])
        
        distances_from_all_centers = [[] for i in range(len(self.data))]

        #distances for each point in list
        for i in range(len(self.data)):
            for key in initial_centers: 
                distances_from_all_centers[i].append(distances[key][i])
        
        #index + 1 of the minimum 
        indices = []
        for entries in distances_from_all_centers: 
            indices.append(entries.index(min(entries)))

        dictionary_points = [num + 1 for num in indices ]

        new_clusters = {}
        for key in self.clusters: 
            new_clusters[key] = []

        #reassigning points
        for key in new_clusters: 
            for i in range(len(dictionary_points)): 
                if dictionary_points[i] == key: 
                    new_clusters[key].append(i)
        

        if new_clusters != self.clusters: 
            self.clusters = new_clusters
            self.run()
        else: 
            return self.clusters
        


   