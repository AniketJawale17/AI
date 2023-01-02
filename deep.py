import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from matplotlib import  pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv("C:/Users/Hp/Desktop/Practicles/ML/pract8/diabetes2.csv")
print(data.head(5))

import seaborn as sns
print(data['Outcome'].value_counts().plot(kind = 'bar'))
plt.show()

predictors = data.iloc[:,0:8]
response = data.iloc[:,8]

x_train,x_test,y_train,y_test = train_test_split(predictors,response,test_size=0.2)
print(x_train.shape,y_train.shape)
print(x_train.shape,y_test.shape)

kerasmodel = Sequential()
kerasmodel.add(Dense(20,input_dim=8,activation='relu'))
kerasmodel.add(Dense(8,activation='relu'))
kerasmodel.add(Dense(1,activation='sigmoid'))

kerasmodel.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model=kerasmodel.fit(x_train,y_train,epochs=300,batch_size=15)

_, accuracy = kerasmodel.evaluate(x_train,y_train)
print('Train Accuracy: %2f' % (accuracy*100))

from sklearn.metrics import  accuracy_score
y_pred = kerasmodel.predict(x_test)
y_pred = np.round(y_pred).astype(int)

accuracy_score(y_test,y_pred)

from ann_visualizer.visualize import ann_viz

ann_viz(kerasmodel, title="Diabetes prediction")