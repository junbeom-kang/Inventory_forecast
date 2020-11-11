import folium
import pandas as pd
import matplotlib.pyplot as plt
def change(x):
    s=str(x)
    if s[0]=='제':
        return 'Jeju'
    elif s[0:2]=='경기':
        return 'Gyeonggi'
    elif s[0]=='강':
        return 'Gangwon'
    elif s[0]=='경':
        if s[1]=='남' or s[2]=='남':
            return 'Gyeongnam'
        else:
            return 'Gyeongbuk'
    elif s[0]=='충':
        if s[1]=='남' or s[2]=='남':
            return 'Chungnam'
        else:
            return 'Chungbuk'
    elif s[0]=='전':
        if s[1]=='남' or s[2]=='남':
            return 'Jeonnam'
        else:
            return 'Jeonbuk'

df=pd.read_csv('C:/User/camping_loc.csv',encoding='cp949')
df=df.filter(['주소'])

df['rename']=df['주소'].apply(change)

temp=df.groupby(df['rename']).count()
plt.figure(figsize=(12,6))
plt.xlabel('Region')
plt.ylabel('Count')
plt.bar(temp.index,temp['주소'])
plt.show()