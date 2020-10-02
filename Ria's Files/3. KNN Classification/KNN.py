import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

p1=[2,4]
p2=[4,2]
p3=[4,4]
p4=[4,6]
p5=[6,2]
p6=[6,4]
x=[p1,p2,p3,p4,p5,p6]
y=[0,0,1,0,1,0] # 0 for orange and 1 for blue

classifier=KNeighborsClassifier(n_neighbors=4,p=2,metric='minkowski')

classifier.fit(x,y)

#x_pred=np.array([6,6])
x_pred=np.array([6,6])
y_pred=classifier.predict(x_pred.reshape(1,-1))

plt.scatter(p1[0],p1[1],c='orange',marker='s')
plt.scatter(p2[0],p2[1],c='orange',marker='s')
plt.scatter(p3[0],p3[1],c='blue',)
plt.scatter(p4[0],p4[1],c='orange',marker='s')
plt.scatter(p5[0],p5[1],c='blue')
plt.scatter(p6[0],p6[1],c='orange',marker='s')

if(y_pred==0):
    color='orange'
    marker='s'
else:
    color='blue'
    marker='.'
    
plt.scatter(x_pred[0],x_pred[1],c=color,marker=marker,s=400)
print("Point (6,6) gets classified as ",color," using averaging KNN")
plt.savefig('output')
plt.show()

## just for distance weighted

classifier=KNeighborsClassifier(n_neighbors=4,p=2,weights='distance',metric='minkowski')

classifier.fit(x,y)

#x_pred=np.array([6,6])
x_pred=np.array([6,2])
y_pred=classifier.predict(x_pred.reshape(1,-1))

plt.scatter(p1[0],p1[1],c='orange',marker='s')
plt.scatter(p2[0],p2[1],c='orange',marker='s')
plt.scatter(p3[0],p3[1],c='blue',)
plt.scatter(p4[0],p4[1],c='orange',marker='s')
plt.scatter(p5[0],p5[1],c='blue')
plt.scatter(p6[0],p6[1],c='orange',marker='s')

if(y_pred==0):
    color='orange'
    marker='s'
else:
    color='blue'
    marker='.'
    
plt.scatter(x_pred[0],x_pred[1],c=color,marker=marker,s=600)
print("Point (6,6) gets classified as ",color," using distance Weighted KNN")
plt.savefig('output1')
plt.show()




