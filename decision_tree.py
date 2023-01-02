import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/Hp/Desktop/Practicles/ML/pract5/PlayTennis.csv")
#print(data.columns  )

from sklearn.preprocessing import LabelEncoder
data['outlook']=LabelEncoder().fit_transform(data['outlook'])
data['temp']=LabelEncoder().fit_transform(data['temp'])
data['humidity']=LabelEncoder().fit_transform(data['humidity'])
data['windy']=LabelEncoder().fit_transform(data['windy'])
data['play']=LabelEncoder().fit_transform(data['play'])
#print(data)
y= data['play']
x = data.drop(['play'],axis=1)
from sklearn import tree
dt=tree.DecisionTreeClassifier(criterion="entropy")
dt=dt.fit(x,y)
tree.plot_tree(dt)
plt.show()