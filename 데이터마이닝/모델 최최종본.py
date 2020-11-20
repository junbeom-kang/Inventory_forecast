from keras import models
from keras import layers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import ceil
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

df = df[['Holiday', 'Weather','Peo_T','Avg_T','Min_T', 'Max_T',]]
x = df[:]

mean = x.mean(axis=0)
x -= mean
std = x.std(axis=0)
x /= std


ICRmodel = build_model()
Cakemodel = build_model()
Shakemodel = build_model()

ICRhistory = ICRmodel.fit(x, ICR, epochs=1000, batch_size=10, verbose=0)
Cakehistory = Cakemodel.fit(x, Cake, epochs=1000, batch_size=10, verbose=0)
Shakehistory = Shakemodel.fit(x, Shake, epochs=1000, batch_size=10, verbose=0)
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

next_day=[[]]
next_day[0].append(float(input("주말 여부를 입력하세요(공휴일2 주말1 아니면 0)")))
next_day[0].append(float(input("날씨 정보를 입력하세요(비가온다면 1 아니면 0)")))
next_day[0].extend(map(float,input("온도 정보를 입력하세요(평균,체감,최소,최고)").split()))
stock=list(map(float,input('아이스크림,케이크,쉐이크의 재고를 입력하세요').split()))
next_day,stock=np.array(next_day),np.array(stock)
next_day-=mean
next_day/=std
needICR=ceil(ICRmodel.predict(next_day)[0][0]-stock[0]+mean_squared_error(ICR, ICR_hat))+1
needCake=ceil(Cakemodel.predict(next_day)[0][0]-stock[1]+mean_squared_error(Cake, Cake_hat))+1
needShake=ceil(Shakemodel.predict(next_day)[0][0]-stock[2]+mean_squared_error(Shake, Shake_hat))+1

print('아이스크림 필요 주문량은',needICR,'입니다')
print('케이크 필요 주문량은',needCake,'입니다')
print('쉐이크 필요 주문량은',needShake,'입니다')






