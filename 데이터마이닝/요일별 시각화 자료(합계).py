import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('May.csv',thousands = ',')
b = pd.read_csv('July.csv', thousands = ',')
c = pd.read_csv('September.csv', thousands = ',')

may = pd.DataFrame(a[:7], columns = ['요일별평균일매출(NET)'])
may.index = ['일','월','화','수','목','금','토']

july = pd.DataFrame(b[:7],columns = ['요일별평균일매출(NET)'])
july.index = ['일','월','화','수','목','금','토']

september = pd.DataFrame(c[:7],columns = ['요일별평균일매출(NET)'])
september.index =['일','월','화','수','목','금','토']

total = may + july + september
plt.bar(total.index, total['요일별평균일매출(NET)'],width = 0.25, label = '5월~10월(합계)')
plt.rc('font', family='Malgun Gothic')
plt.xlabel('요일')
plt.ylabel('매출')
plt.legend()