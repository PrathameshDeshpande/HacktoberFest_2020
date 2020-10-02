import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

P1=[0.1,0.6]
P2=[0.15,0.71]
P3=[0.08,0.9]
P4=[0.16,0.85]
P5=[0.2,0.3]
P6=[0.25,0.5]
P7=[0.24,0.1]
P8=[0.3,0.2]

x=[P1,P2,P3,P4,P5,P6,P7,P8]
x=np.array(x)

plt.scatter(P1[0],P1[1],c='black',label='P1')
plt.scatter(P2[0],P2[1],c='black',label='P2',marker='s',s=100)
plt.scatter(P3[0],P3[1],c='black',label='P3',marker='1',s=200)
plt.scatter(P4[0],P4[1],c='black',label='P4',marker='2',s=200)
plt.scatter(P5[0],P5[1],c='black',label='P5',marker='3',s=200)
plt.scatter(P6[0],P6[1],c='black',label='P6',marker='4',s=200)
plt.scatter(P7[0],P7[1],c='black',label='P7',marker='o',s=200)
plt.scatter(P8[0],P8[1],c='black',label='P8',marker='x',s=100)
plt.title('Points in the dataset')
plt.legend()

kmeans=KMeans(n_clusters=2,init='k-means++',max_iter=300,n_init=10,random_state=0)
y_kmeans=kmeans.fit_predict(x)

plt.show()

plt.scatter(x[y_kmeans==0,0],x[y_kmeans==0,1],s=100,c='red',label='cluster 1')
plt.scatter(x[y_kmeans==1,0],x[y_kmeans==1,1],s=100,c='blue',label='cluster 2')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='centroids')
plt.scatter(P6[0],P6[1],c='black',label='P6')
plt.title('Clustering')
plt.legend()
#Question 1
print("point p6 belongs to ",end=" ")
if y_kmeans[5]==0:
	print("cluster 1")
else:
	print("cluster 2")
#Question 2
print("the population of cluster around m2 ie C2 ==>",end=" ")
counter = 0
for i in y_kmeans:
	if i == 1:
		counter = counter + 1;
print(counter)
#Question 3
C_list = kmeans.cluster_centers_[:,[0,1]]
print("Centroid C1 = ",C_list[0],"& Centroid C2 = ",C_list[1])

plt.show()

