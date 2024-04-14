import numpy as np
from sklearn.cluster import KMeans as ScikitLearnKMeans
from sklearn.datasets import make_blobs, make_moons, make_circles
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=100, centers=3, random_state=10)
# X, y = make_moons(n_samples=100, random_state=10)
# X, y = make_circles(n_samples=100, random_state=10)
colors = ['r', 'g', 'b', 'c', 'y']


def k_mean(X, k=3, iter=10, min_dist=0.1):
    np.random.seed(3)
    centroids = np.random.choice(X.shape[0], k, replace=False)
    centroid_coords = X[centroids]
    for i in range(iter):
        clusters = {i: [] for i in range(k)}
        for x in X:
            dist = np.linalg.norm(centroid_coords - x, axis=1)
            clusters[dist.argmin()].append(x)
        new_cent = {}
        for i in clusters:
            new_cent[i] = np.mean(clusters[i], axis=0)
        new_cent = dict(sorted(new_cent.items()))
        new_cent = np.array(list(new_cent.values()))

        if np.max(np.linalg.norm(centroid_coords - new_cent)) < min_dist:
            print(i)
            break
        centroid_coords = new_cent.copy()
    print('all_iter')
    return clusters, centroids

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

clusters, centroids = k_mean(X)

for i in clusters:
    for_plt = np.array(clusters[i]).T
    axs[0].scatter(for_plt[0], for_plt[1], c=colors[i])
axs[0].set_title('Custom KMeans')


scikit_kmeans = ScikitLearnKMeans(n_clusters=3)
scikit_kmeans.fit(X)
scikit_kmeans_labels = scikit_kmeans.predict(X)

for i in range(len(scikit_kmeans_labels)):
    axs[1].scatter(X[i, 0], X[i, 1], c=colors[scikit_kmeans_labels[i]])
axs[1].set_title('Scikit-Learn KMeans')

# print(scikit_kmeans)

plt.show()
