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


df = pd.read_csv('C:/User/data123.csv',encoding='cp949')
CUV = df['cumulative UV']
MUV = df['Maximum UV']


df = df[['Aerosol','Temp_avg','Temp_min','Temp_max', 'Humidity','sunshine time','Total daylight hours','cloud cover']]
CUV_X_train, CUV_X_test, CUV_Y_train, CUY_Y_test = train_test_split(df, CUV, test_size=0.2, shuffle=True, random_state=1234)
MUV_X_train, MUV_X_test, MUV_Y_train, MUV_Y_test = train_test_split(df, MUV, test_size=0.2, shuffle=True, random_state=1234)

CUVModel = build_model()
MUVModel = build_model()

CUV_history = CUVModel.fit(df, CUV, epochs=100, batch_size=10, verbose=0)
MUV_history = MUVModel.fit(df, MUV, epochs=100, batch_size=10, verbose=0)

CUV_hat = CUVModel.predict(CUV_X_test)
MUV_hat = MUVModel.predict(MUV_X_test)


plt.figure(figsize=(12,4))
plt.suptitle('MSE according to epoch ',fontsize=20)
plt.subplot(1,2,1)
plt.ylabel('mse')
plt.xlabel('epoch')
plt.title('CUV', fontsize=10)
plt.plot(CUV_history.history['loss'])
plt.subplot(1,2,2)
plt.ylabel('mse')
plt.xlabel('epoch')
plt.title('MUV', fontsize=10)
plt.plot(MUV_history.history['loss'])
#plt.show()

print(mean_squared_error(CUV_hat, CUY_Y_test))
print(mean_squared_error(MUV_hat, MUV_Y_test))
