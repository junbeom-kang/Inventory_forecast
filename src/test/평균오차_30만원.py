from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from keras import models
from keras import layers
import tensorflow as tf
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(300, activation='relu',
                           input_shape=(x_train.shape[1],)))
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(100, activation='relu'))
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mse'])
    return model

df=pd.read_csv('C:/User/Data.csv')
df['Sale']=df['Sale'].map(lambda x:x.replace(',',''))
y=df['Sale'].astype(float)
df=df[['Avg_T','Holiday','Weather']]
df.head()
#x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.3)
x=df[:]
x_train,y_train=df[:120],y[:120]
x_test,y_test=df[120:],y[120:]
x_test.head()
y_train.head()
x_train.head()
y_test.head()
#정규화
'''
mean = x_train.mean(axis=0)
x_train -= mean
std = x_train.std(axis=0)
x_train/= std
x_test -= mean
x_test /= std
x_train.head()
x_test.head()
'''

#모델만들고 fit
model = build_model()

model.fit(x_train,y_train,epochs=5000,batch_size=10, verbose=2)
y_hat=model.predict(x_train)

test_mse_score, test_mae_score = model.evaluate(y_hat, y_train)
print(test_mse_score)