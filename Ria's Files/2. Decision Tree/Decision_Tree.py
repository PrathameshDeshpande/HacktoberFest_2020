from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pandas as pd
import numpy as np

dataset=pd.read_csv("assign2DataAll.csv")
x=dataset.iloc[0:15,:-1]        #Reading all rows 
y=dataset.iloc[:14,5]           #Reading first 14 rows only 5th coloumn (from 0)

print("\nAll Data\n\n",x)

le=LabelEncoder()
lx=x.apply(le.fit_transform)

regressor=DecisionTreeClassifier()
regressor.fit(lx.iloc[:14,1:5],y)        #Fitting only first 14 rows with label

x_test = lx[14:]                         #14 above till last for test (not 14)

print("\nTest Data\n\n",x_test)
x_test=sum(x_test.values.tolist(),[])   #for conversion of df to list

x_test =x_test[1:]                      

y_pred=regressor.predict([x_test])
print("\nFor test data:\n",x[14:])      
print("Output: Prediction is ",y_pred)

export_graphviz(regressor, out_file ='tree.dot')        #text graph

#sudo apt install graphviz
#dot -Tpng tree.dot -o tree.png
