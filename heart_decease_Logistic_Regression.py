# -*- coding: utf-8 -*-
"""Heart.deceaseLOR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TE9XuMc3OqzZAKh0_VdOtwAtPKvblFKg
"""

import pandas as pd
import numpy as np
df=pd.read_csv("/content/framingham.csv")
df

df.head(4)

x=df[['totChol','sysBP','diaBP','BMI','heartRate','glucose']]
y=df[['TenYearCHD']]
print(x)
print(y)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
x_train,xtest,y_train,y_train =train_test_split(x,y ,test_size=0.2)
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
y_pred=logreg.predict(x_test)
print(y_pred)

from sklearn import preprocessing
fruits=["apple","mango","apple","apple","mango","mango"]
label_encoder=preprocessing.LabelEncoder()
encoded=label_encoder.fit_transform(fruits)
print(encoded)