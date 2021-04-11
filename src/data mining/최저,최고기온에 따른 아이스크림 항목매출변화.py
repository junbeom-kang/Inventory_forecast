import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def drop_last(temp):
    temp=temp.drop(temp.index[-1])
    return temp

df5=pd.read_excel('C:/User/5.xlsx')
df5=drop_last(df5)
df6=pd.read_excel('C:/User/6.xls')
df6=drop_last(df6)
df7=pd.read_excel('C:/User/7.xls')
df7=drop_last(df7)
df8=pd.read_excel('C:/User/8.xls')
df8=drop_last(df8)
df9=pd.read_excel('C:/User/9.xls')
df9=drop_last(df9)
df10=pd.read_excel('C:/User/10.xls')
df10=drop_last(df10)
df=pd.concat([df5,df6,df7,df8,df9,df10],axis=0)

df['new']=df['온도(최저/최고)▲'].str.split('/')
df['a']=df['new'].str[0].astype(float)//1
df['b']=df['new'].str[1].astype(float)//1

data=df.loc[df['대분류명']=='아이스크림&빙수']
low=data['총매출금액'].groupby(data['a']).mean()
high=data['총매출금액'].groupby(data['b']).mean()

plt.figure(figsize=(12, 8))
plt.suptitle('Relationship between temperature and sales',fontsize=20)
plt.subplot(2,1,1)
plt.title('Sales by lowest temperature', fontsize=10)
plt.bar(low.index,low)
plt.xticks(low.index)
plt.ylabel('million won')
plt.xlabel('low temperature(degree Celsius ℃)')

plt.subplot(2,1,2)
plt.title('Sales by highest temperature', fontsize=10)
plt.bar(high.index,high)
plt.xticks(high.index)
plt.ylabel('million won')
plt.xlabel('low temperature(degree Celsius ℃)')
plt.subplots_adjust(hspace=0.3)
plt.show()
