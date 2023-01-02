#Assignment based on simple linear regression on any dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  sklearn.linear_model import LinearRegression
data=pd.read_csv("C:/Users/Hp/Desktop/Practicles/ML/pract4/houseprices.csv")
#print(data.columns)
f=['Price', ' Area']
data=data[f]
#print(data)
x=data.iloc[:,1:].values
print("independent variable area as x \n",x)
y=data.iloc[:,:1].values
print("Dependent variable price as y \n", y)
#split data into training and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=3)
#print(x_train)
reg=LinearRegression()
reg.fit(x_train,y_train)
prediction=reg.predict(x_test)
print(prediction)
print(y_test)
#calculating mse,rmse and r-squre
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,prediction)
print("mean squeare error: \n",mse)
r2score=reg.score(x_test,y_test)
print(r2score)
print("weight or slope M is : \n",reg.coef_)
print("intercept C is :\n",reg.intercept_)
plt.scatter(x_test,y_test)
plt.plot(x_test, prediction, color = "g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

