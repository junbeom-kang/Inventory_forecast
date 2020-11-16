from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from keras import models
from keras import layers
import tensorflow as tf
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(x_train.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

df=pd.read_csv('C:/User/Data.csv')
df['Sale']=df['Sale'].map(lambda x:x.replace(',',''))
y=df['Sale'].astype(float)
df=df[['Avg_T','Holiday','Weather']]
type(df)
type(y)
df.head()
x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.3)

#정규화

mean = x_train.mean(axis=0)
x_train -= mean
std = x_train.std(axis=0)
x_train/= std
x_test -= mean
x_test /= std
x_train.head()
x_test.head()

y_train
#모델만들고 fit
model = build_model()
x_train.shape
y_train.shape
model.fit(x_train,y_train,epochs=8000, verbose=2)
y_hat=model.predict(x_test)
#plt.plot(y)
plt.plot(y_hat)
plt.plot(y_test)
plt.show()

test_mse_score, test_mae_score = model.evaluate(x_test, y_test)
print(test_mae_score)