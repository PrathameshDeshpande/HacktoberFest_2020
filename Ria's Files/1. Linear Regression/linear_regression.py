import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv(r'hours.csv')
#info regarding dataset (total no. of columns, rows and their respective datatypes) 
data.info()
#statistical information about the dataset
data.describe()

#After reading the dataset, the total no of rows and columns read is described using .shape method
data.shape

#Selecting the dependent attribute/ predictor
x = data[['hours_spent']]

#Selecting the Independent attribute 
y = data['risk_score']

# Splitting the dataset into training and testing.
# 10% of the dataset is used for testing and 90% of dataset is used for training
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.1,random_state = 0)

#Creating an instance of class LinearRegression 
reg = LinearRegression()  

# fits a linear model
# Train model using training sets i.e using x_train and y_train
reg.fit(x_train,y_train)    

# Make predictions using testing data i.e x_test 
# .predict method is used to predict the values for the testing data. 
y_pred = reg.predict(x_test)

print(reg.coef_)
print(reg.intercept_)

#Printing the predicted and actual values
print(y_pred)
print(y_test)

# Plotting the training data-points and best fit line.
plt.scatter(x_train,y_train, color='red')
plt.plot(x_train, reg.predict(x_train), color='green')
plt.title('Linear Regression')
plt.xlabel('hours_spent')
plt.ylabel('risk_score')
plt.savefig('output')
plt.show()    

# To check the accuracy of the model.
# Metrics used for evaluation of trained model in case is Regression are :
# Mean Absolute Error = |actual - predicted|
# Mean Squared Error = |actual - predicted|^2
# Root Mean Squared Error = sqrt(|actual - predicted^2|)
from sklearn import metrics
import numpy as np
print('Mean Absolute Error = ',metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error = ',metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Square Error = ',np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

