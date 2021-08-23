# N-Dimensional Clustering Spatial Data Mining Algorithm

> Spatial data mining is the process of discovering interesting and previously unknown, but potentially useful patterns from spatial databases.

### Algorithm input:

- Dimensions (d)
- Threshold distance (t)
- Array of N Points

### Algorithm output:

- Array of Clusters

### Clusters

A cluster has the following structure:

```py
{
	"mean_point": [X1, X2, X3, ... Xd],
	"points": [[X11, X12, X13, ... X1d], [X2, X22, X23, ... X2d], ...]
}
```
Each point in the cluster is at least `t` distance away from the `mean_point`. 

### Time and Space Complexity
- Time: `O(d * N^2)`
- Space: `O(d * N)`

### Pseudo code

```
def Algorithm(points, t, d):
	Clusters = empty set
	for each P in points do:
		if Clusters is empty set:
			Make a new cluster with P
		else:
			best_match_cluster = None
			for each C in Clusters do:
				if dist(C.mean_point, P) <= t and best_match_cluster distance > dist(C.mean_point, P):
					best_match_cluster = C
			if best_match_cluster is None:
				Make a new cluster with P
			else:
				add P to best_match_cluster and update the mean point
	return Clusters
```