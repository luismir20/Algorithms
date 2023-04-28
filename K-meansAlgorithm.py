import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = np.array([
    [1, 2],
    [1.5, 1.8],
    [5, 8],
    [8, 8],
    [1, 0.6],
    [9, 11]
])

# Number of clusters
k = 2

# KMeans instance with the specified number of clusters
kmeans = KMeans(n_clusters=k)


kmeans.fit(data)

centroids = kmeans.cluster_centers_

# Cluster assignments for each data point
labels = kmeans.labels_

print("Cluster centroids:\n", centroids)
print("Cluster assignments:", labels)

plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-means Clustering')
plt.show()
