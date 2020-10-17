import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_excel('C:/User/5.xlsx')
df=df.drop(268)
qwer=df['총매출금액'].groupby(df['온도(최저/최고)▲']).sum()
temp=pd.DataFrame(qwer,index=qwer.index)
#temp
temp['new']=qwer.index
#temp.columns


temp['a']=temp['new'].str.split('/').str[0].astype(float)//3
temp['b']=temp['new'].str.split('/').str[1].astype(float)//3
temp['c']=(temp['a']*3).astype(str)+'~'+(temp['b']*3).astype(str)

''''''
abc=temp['총매출금액'].groupby(temp['c']).mean()
a=abc.index

plt.figure(figsize=(16, 5))
plt.title('Sales by temperature', fontsize=20)
plt.bar(abc.index,abc)
plt.xticks(abc.index,a)
plt.ylabel('million won')
plt.xlabel('low~high temperature(degree Celsius ℃)')
plt.show()