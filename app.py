import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

data=pd.read_csv(r'D:\VS_CODE(PROJECTS-NARESH-IT)\Ensamble learning\Churn_Modelling.csv')

x=data.iloc[:,3:-1].values
y=data.iloc[:,-1].values
#print(y)
#print(x)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
x[:,2]=le.fit_transform(x[:,2])

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder='passthrough')
x=np.array(ct.fit_transform(x))

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from xgboost import XGBClassifier
classifier=XGBClassifier()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
print(cm)

acc=accuracy_score(y_test,y_pred)
print(acc)

pickle.dump(classifier,open('model.pkl','wb'))

