import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
temp=pd.read_csv('C:/User/nba.csv',delimiter=',')
#마지막 값이 NaN으로 떠서 -1로 설정
#plt.hist(temp.Age[:-1])
#plt.show()

#print(temp.loc[temp.Salary.idxmax()])

team=temp['Salary'].groupby(temp['Team'])
plt.bar(range(len(team)),team.mean())
plt.xlabel('Team')
plt.ylabel('Salary')
#plt.show()
print('Avg Age:',temp['Age'].mean())
print('Avg Salary:',temp['Salary'].mean())

#print(temp.College.value_counts())

#for position,group in temp.groupby('Position'):
#    print(group['Name'])