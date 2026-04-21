import pandas as pd
from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt

from data_generator.data_perparation import data_preparation

def optimal_kmeans_clusters(x_scaled, max_k=10):
    inertias = [KMeans(n_clusters=k, random_state=42, n_init=10).fit(x_scaled).inertia_ for k in range(1, max_k + 1)]

    kl = KneeLocator(
        x=range(1, max_k + 1),
        y=inertias,
        curve="convex",
        direction="decreasing"
    )
    plt.plot(range(1, max_k + 1), inertias)
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Inertia")
    plt.title("Elbow Method for Optimal k")
    plt.savefig("Placement_readiness\\reports\\visuals\\elbow_plot.png")
    plt.close()
    return kl.elbow 
def train_kmeans_model(x_scaled, n_clusters):
    model = KMeans(n_clusters=n_clusters, random_state=42 , n_init=10)
    clusters = model.fit_predict(x_scaled)

    return model , pd.Series(clusters, index=x_scaled.index, name='cluster')


df = data_preparation(100)
print(df)