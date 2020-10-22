import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

Main5 = pd.read_csv('C:/5.csv')
Main6 = pd.read_csv('C:/6.csv')
Main7 = pd.read_csv('C:/7.csv')
Main8 = pd.read_csv('C:/8.csv')
Main9 = pd.read_csv('C:/9.csv')

x5 = Main5['Day']
y5 = Main5['Weather']
x6 = Main6['Day']
y6 = Main6['Weather']
x7 = Main7['Day']
y7 = Main7['Weather']
x8 = Main8['Day']
y8 = Main8['Weather']
x9 = Main9['Day']
y9 = Main9['Weather']

plt.figure(figsize=(15,6))
plt.suptitle('The day it rained')
plt.subplot(3,2,1)
plt.title("May")
plt.bar(x5,y5)
plt.xticks(x5, ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'])
plt.yticks(y5)

plt.subplot(3,2,2)
plt.title("June")
plt.bar(x6,y6)
plt.xticks(x6, ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'])
plt.yticks(y6)

plt.subplot(3,2,3)
plt.title("July")
plt.bar(x7,y7+1)
plt.xticks(x7, ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']) 
plt.yticks(y7)

plt.subplot(3,2,4)
plt.title("August")
plt.bar(x8,y8)
plt.xticks(x8, ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']) 
plt.yticks(y8)

plt.subplot(3,2,5)
plt.title("September")
plt.bar(x9,y9)
plt.xticks(x9, ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'])
plt.yticks(y9)
plt.subplots_adjust(hspace=0.5)
plt.show()

