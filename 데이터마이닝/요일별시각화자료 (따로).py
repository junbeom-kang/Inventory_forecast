import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('May.csv', thousands=',')
b = pd.read_csv('July.csv', thousands=',')
c = pd.read_csv('September.csv', thousands=',')

may = pd.DataFrame(a[:7], columns=['요일별평균일매출(NET)'])
may.index = ['일', '월', '화', '수', '목', '금', '토']

july = pd.DataFrame(b[:7], columns=['요일별평균일매출(NET)'])
july.index = ['일', '월', '화', '수', '목', '금', '토']

september = pd.DataFrame(c[:7], columns=['요일별평균일매출(NET)'])
september.index = ['일', '월', '화', '수', '목', '금', '토']

plt.figure()

may = pd.DataFrame(a[:7], columns=['요일별평균일매출(NET)'])
may.index = ['일', '월', '화', '수', '목', '금', '토']
plt.bar(may.index, may['요일별평균일매출(NET)'], width=0.25, label='5월~6월')
plt.bar(july.index, july['요일별평균일매출(NET)'], width=0.25, label='7월~8월')
plt.bar(september.index, september['요일별평균일매출(NET)'], width=0.25, label='9월~10월')
plt.legend()