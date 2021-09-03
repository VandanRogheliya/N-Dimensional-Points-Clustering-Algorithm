import math
import csv


class single_scan:
    """ Takes points in N dimension space as an input and a threshold distance to form clusters. Time: O(d * n ^ 3) , Space: O(d * n) """
    #! INPUT:
    # Dimensions
    dimension = 3

    # Array of points in space
    # [(x1, y1, z1), (x2, y2, z2), ...]
    points = []

    # threshold distance used to form clusters
    threshold_clustering_distance = math.inf

    # threshold distance used to form relations
    threshold_relationship_distance = math.inf

    #! OUTPUT:
    # Clusters in space
    # [{ (cx1, cy1, cz1), (cx2, cy2, cz2), ... }, ...]
    clusters = []

    def calculate_distance(self, pointA, pointB):
        sum = 0
        for i in range(0, self.dimension):
            sum += pow(pointA[i] - pointB[i], 2)
        return math.sqrt(sum)

    def get_neighbours(self, current_point):
        neighbours = set()
        for point in self.points:
            if self.calculate_distance(point, current_point) <= self.threshold_relationship_distance:
                neighbours.add(point)
        return neighbours

    def are_neighbours_satisfy_clustering_condition(self, current_point, neighbours):
        for point in neighbours:
            if self.calculate_distance(current_point, point) > threshold_clustering_distance:
                return False
        return True

    def make_clusters(self):
        processed_points = set()
        current_objects = set()
        # Points that represent a cluster
        cluster_points = set()
        for point in self.points:
            if point in cluster_points:
                continue
            current_objects.add(point)
            new_cluster = set()
            while current_objects:
                current_point = current_objects.pop()
                if current_point in processed_points:
                    continue
                processed_points.add(current_point)
                neighbours = self.get_neighbours(current_point)
                if self.are_neighbours_satisfy_clustering_condition(current_point, neighbours):
                    new_cluster.add(current_point)
                    current_objects = current_objects.union(neighbours)
            if new_cluster:
                self.clusters.append(new_cluster)

    def __init__(self, points, threshold_clustering_distance, threshold_relationship_distance, dimension):
        self.points = points
        self.threshold_clustering_distance = threshold_clustering_distance
        self.threshold_relationship_distance = threshold_relationship_distance
        self.dimension = dimension

        self.make_clusters()


csv_file = open('500-random-25-dimensional-points.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

lines = 0

# Control input here
NUMBER_OF_POINTS = 10
threshold_clustering_distance = 20
threshold_relationship_distance = 30
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

spatialCluster = single_scan(
    points, threshold_clustering_distance, threshold_relationship_distance, DIMENSIONS)
print('Input:')
points.sort()
for point in points:
    print(point)
print('No. of clusters:', len(spatialCluster.clusters))
for cluster in spatialCluster.clusters:
    print(cluster)
