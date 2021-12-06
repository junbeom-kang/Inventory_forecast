from keras import models
from keras import layers
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

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


df = pd.read_csv('C:/User/indata123.csv',encoding='cp949')
UV_sensor = df['uv_sensor']//10
Volts=df['volts']


df = df[['Temp_avg','Temp_min','Temp_max', 'Humidity','cloud cover','uv index']]
x = df[:]
UV_sensor_train, UV_sensor_test, UV_sensor_Y_train, UV_sensor_Y_test = train_test_split(df, UV_sensor, test_size=0.2, shuffle=True, random_state=1234)
UV_sensorModel = build_model()
UV_sensor_history = UV_sensorModel.fit(UV_sensor_train, UV_sensor_Y_train, epochs=300, batch_size=10, verbose=2)

UV_sensor_hat = UV_sensorModel.predict(UV_sensor_test)
print(mean_squared_error(UV_sensor_hat, UV_sensor_Y_test))
print((mean_squared_error(UV_sensor_hat, UV_sensor_Y_test))**0.5)
"""
plt.figure(figsize=(12,4))
plt.suptitle('MSE according to epoch ',fontsize=20)
plt.subplot(1,2,1)
plt.ylabel('mse')
plt.xlabel('epoch')
plt.title('CUV', fontsize=10)
plt.plot(UV_sensor_history.history['loss'])
plt.show()
"""





