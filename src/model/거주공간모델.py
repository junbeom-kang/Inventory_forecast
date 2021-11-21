from keras import models
from keras import layers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import ceil

from sklearn.model_selection import train_test_split


def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',input_shape=(df.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])
    return model


df = pd.read_csv('C:/User/data123.csv',encoding='cp949')
UV = df['UV index']



df = df[['Aerosol','Temp_avg','Temp_min','Temp_max', 'Humidity','sunshine time','cloud cover']]
x = df[:]
UV_X_train, UV_X_test, UV_Y_train, UY_Y_test = train_test_split(df, UV, test_size=0.2, shuffle=True, random_state=1234)

CUVModel = build_model()
MUVModel = build_model()

CUV_history = CUVModel.fit(UV_X_train, UV_Y_train, epochs=100, batch_size=10, verbose=2)
MUV_history = MUVModel.fit(UV_X_train, UV_Y_train, epochs=100, batch_size=10, verbose=2)

CUV_hat = CUVModel.predict(UV_X_test)
MUV_hat = MUVModel.predict(UV_X_test)


plt.figure(figsize=(12,4))
plt.suptitle('MSE according to epoch ',fontsize=20)
plt.subplot(1,1,1)
plt.ylabel('mse')
plt.xlabel('epoch')
plt.title('CUV', fontsize=10)
plt.plot(CUV_history.history['loss'])

plt.show()
print(mean_squared_error(CUV_hat, UY_Y_test))







