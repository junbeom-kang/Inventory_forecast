from keras import models
from keras import layers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',input_shape=(x.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])
    return model


df = pd.read_csv('C:/User/Data2.csv')
df = df.drop([153])
ICR = df['ICR']
Cake = df['Cake']
Shake = df['Shake']

df = df[['Holiday', 'Weather', 'Min_T', 'Max_T', 'Peo_T','Avg_T']]
x = df[:]

mean = x.mean(axis=0)
x -= mean
std = x.std(axis=0)
x /= std
x.head
# 모델만들고 fit

ICRmodel = build_model()
Cakemodel = build_model()
Shakemodel = build_model()

ICRhistory = ICRmodel.fit(x, ICR, epochs=800, batch_size=10, verbose=0)
Cakehistory = Cakemodel.fit(x, Cake, epochs=800, batch_size=10, verbose=0)
Shakehistory = Shakemodel.fit(x, Shake, epochs=800, batch_size=10, verbose=0)
ICR_hat = ICRmodel.predict(x)
Cake_hat = Cakemodel.predict(x)
Shake_hat = Shakemodel.predict(x)
plt.figure(figsize=(12,4))
plt.suptitle('MSE according to epoch ',fontsize=20)
plt.subplot(1,3,1)
plt.ylabel('mse')
plt.xlabel('epoch')
plt.title('ICR', fontsize=10)
plt.plot(ICRhistory.history['loss'])
plt.subplot(1,3,2)
plt.ylabel('mse')
plt.xlabel('epoch')
plt.title('Cake', fontsize=10)
plt.plot(Cakehistory.history['loss'])
plt.subplot(1,3,3)
plt.ylabel('mse')
plt.xlabel('epoch')
plt.title('Shake', fontsize=10)
plt.plot(Shakehistory.history['loss'])

print("Ice cream mean_squared_error=",mean_squared_error(ICR, ICR_hat))
print("Cake mean_squared_error=",mean_squared_error(Cake, Cake_hat))
print("Shake mean_squared_error=",mean_squared_error(Shake, Shake_hat))
plt.show()