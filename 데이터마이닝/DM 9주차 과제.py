import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

temp=pd.read_csv('C:/User/nba.csv',delimiter=',')
temp1=pd.concat([temp[temp['Team']=='Boston Celtics'],temp[temp['Team']=='Utah Jazz']])
temp1=temp1[['Age','Salary','Team','Position']]
temp1

sns.boxplot(x="Age", y='Salary', hue="Position", data=temp1)
sns.jointplot(x="Age", y="Salary", data=temp1, kind='reg')
#temp2=temp1.groupby(temp1['Position'])
#temp2
with sns.axes_style('white'):
    g = sns.catplot(x="Age", data=temp1, aspect=4.0, kind='count',hue='Position')
