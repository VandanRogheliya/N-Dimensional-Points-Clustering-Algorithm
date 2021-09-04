import math
import csv


class mean_point_clustering:
    """ Takes points in N dimension space as an input and a threshold distance to form clusters. Time: O(d * n ^ 2), Space: O(d * n) """
    #! INPUT:
    # Dimensions
    dimension = 3

    # Array of points in space
    # [(x1, y1, z1), (x2, y2, z2), ...]
    points = []

    # threshold distance used to form clusters
    threshold_distance = 0

    #! OUTPUT:
    # Clusters in space
    """ 
    [
      { mean_point: [x,y,z], points: [[x1,y1,z1], [x2,y2,z2], ...] }
    ]
    """
    clusters = []

    def calculate_distance(self, pointA, pointB):
        sum = 0
        for i in range(0, self.dimension):
            sum += pow(pointA[i] - pointB[i], 2)
        return math.sqrt(sum)

    def calculate_mean_point(self, prev_mean_point, prev_point_count, new_point):
        new_mean_point = []
        for i in range(0, self.dimension):
            new_mean_point.append(
                (prev_mean_point[i] * prev_point_count + new_point[i]) / (prev_point_count + 1))
        return new_mean_point

    def make_clusters(self):
        for point in self.points:
            if len(self.clusters) == 0:
                self.clusters.append({"mean_point": point, "points": [point]})
            else:
                nearest_cluster_index = -1
                minimum_distance = math.inf
                for index in range(0, len(self.clusters)):
                    cluster = self.clusters[index]
                    current_distance = self.calculate_distance(
                        point, cluster["mean_point"])
                    if current_distance <= self.threshold_distance and minimum_distance > current_distance:
                        minimum_distance = current_distance
                        nearest_cluster_index = index
                if nearest_cluster_index == -1:
                    self.clusters.append(
                        {"mean_point": point, "points": [point]})
                else:
                    self.clusters[nearest_cluster_index]["mean_point"] = self.calculate_mean_point(
                        self.clusters[nearest_cluster_index]["mean_point"],
                        len(self.clusters[nearest_cluster_index]["points"]),
                        point)
                    self.clusters[nearest_cluster_index]["points"].append(
                        point)

    def __init__(self, points, threshold_distance, dimension):
        self.points = points
        self.threshold_distance = threshold_distance
        self.dimension = dimension
        self.make_clusters()


csv_file = open('500-random-25-dimensional-points.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

lines = 0

# Control input here
NUMBER_OF_POINTS = 10
THRESHOLD_DISTANCE = 20
DIMENSIONS = 1

points = []

for rows in csv_reader:
    if lines > NUMBER_OF_POINTS:
        break
    lines += 1
    if lines == 1:
        continue
    points.append(tuple([int(coordinate)
                  for coordinate in rows[1:DIMENSIONS+1]]))

# Initializing algorithm
spatialCluster = mean_point_clustering(points, THRESHOLD_DISTANCE, DIMENSIONS)

# Printing output
print('Input:')
points.sort()
for point in points:
    print(point)
print('No. of clusters: ', len(spatialCluster.clusters))
for cluster in spatialCluster.clusters:
    print(cluster)
