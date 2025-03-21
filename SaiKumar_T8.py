import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Step 2: Select features (Annual Income & Spending Score)
X = df.iloc[:, [3, 4]].values  # Assuming columns 3 & 4 are relevant

# Step 3: Standardize the data (helps K-Means work better)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Find the best number of clusters using the Elbow Method
wcss = []  # List to store "Within-Cluster Sum of Squares"
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)  # Inertia = how compact the clusters are

# Step 5: Plot the Elbow Curve
plt.figure(figsize=(8,5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--', color='b')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS (Inertia)")
plt.title("Elbow Method to Find Optimal Clusters")
plt.show()

# Step 6: Apply K-Means with the chosen number of clusters (let’s say 5)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)  # Assigns each point to a cluster

# Step 7: Visualizing the clusters
plt.figure(figsize=(8,5))
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=y_kmeans, palette="viridis")
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X', label="Centroids")
plt.xlabel("Annual Income (Scaled)")
plt.ylabel("Spending Score (Scaled)")
plt.legend()
plt.title("Customer Segmentation using K-Means")
plt.show()
