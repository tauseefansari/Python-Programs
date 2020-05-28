import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn.cluster import KMeans

#Random Points
x=[random.randint(10,80) for i in range(30)]
y=[random.randint(10,80) for i in range(30)]

#creating Data Frame
dataFrame=pd.DataFrame({
    'X':x,
    'Y':y
})

#Number of Clusters (Here we use 4 cluster)
kmeans=KMeans(n_clusters=4)
kmeans.fit(dataFrame)

#centeroids and Labels
labels=kmeans.predict(dataFrame)
centeroids=kmeans.cluster_centers_

#Plotting
fig=plt.figure(figsize=(5,5))
colmap={1:'r',2:'g',3:'b',4:'y'}
colors=map(lambda x:colmap[x+1],labels)
colors1=list(colors)
plt.scatter(dataFrame['X'],dataFrame['Y'],color=colors1,alpha=0.5,edgecolors='k')
for idx,centeroid in enumerate(centeroids):
    plt.scatter(*centeroid,color=colmap[idx+1])
plt.ylabel('Y-Axis of Scatter')
plt.xlabel('X-Axis of Scatter')
plt.title('K-Means Clustering')
plt.xlim(0,100)
plt.ylim(0,100)
plt.show()