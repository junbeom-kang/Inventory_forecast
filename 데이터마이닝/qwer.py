from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from keras import models
from keras import layers
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(x.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.3))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['mse'])
    return model

df=pd.read_csv('C:/User/Data2.csv')
y=df['ICR']
df=df[['Avg_T','Holiday','Weather','Min_T','Max_T','Peo_T']]
#df=df[['Avg_T','Holiday','Weather']]
df.head()
#x_train, x_test, y_train, y_test = train_test_split(df, y, test_size=0.3)
x=df[:]
x.shape
#x_train,y_train=df[:120],y[:120]
#x_test,y_test=df[120:],y[120:]

#정규화
#mean = x_train.mean(axis=0)
mean = x.mean(axis=0)

#x_train.head()
x-=mean
#x_train -= mean
#std = x_train.std(axis=0)
std = x.std(axis=0)

#x_train/= std
#x_test -= mean
#x_test /= std
x/=std

#모델만들고 fit
model = build_model()

model.fit(x,y,epochs=5000,batch_size=10, verbose=2)
y_hat=model.predict(x)
#plt.plot(y)
plt.plot(y_hat)
plt.plot(y)
print(mean_squared_error(y,y_hat))
print(mean_absolute_error(y,y_hat))
'''
test_mse_score, test_mae_score = model.evaluate(y_train, y_hat)
print(test_mse_score,test_mae_score)
'''
