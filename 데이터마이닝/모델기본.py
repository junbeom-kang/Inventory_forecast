import keras
from keras import models
from keras import layers
from keras.datasets import boston_housing
import numpy as np
def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(train_data.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['accuracy'])
    return model

#(train_data, train_targets), (test_data, test_targets) =  boston_housing.load_data()
(train_data, train_targets), (test_data, test_targets) =  boston_housing.load_data()
type(train_data[0][0])

#정규화
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std
ttt-=mean
ttt/=std
test_data -= mean
test_data /= std

#데이터 하나 넣고 나오나 보기
ttt=np.array([[-0.27224633, -0.48361547, -0.43576161, -0.25683275, -0.1652266 ,
       -0.1764426 ,  0.81306188,  0.1166983 , -0.62624905, -0.59517003,
        1.14850044,  0.44807713,  0.8252202 ]])

#모델만들고 fit
model = build_model()
model.fit(train_data, train_targets,epochs=80, batch_size=10, verbose=0)
y=model.predict(ttt)
print(y)
#test_mse_score, test_mae_score = model.evaluate(test_data, test_targets)
#print(test_mae_score)