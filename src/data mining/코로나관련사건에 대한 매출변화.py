import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 재난지원금 (5/10~5/20)
pos_givemoney = pd.Series(np.array([24502122,23648032]), index=['5/10~5/20','5/20~5/30'])
#광화문시위
pos_Gwanghwamun=pd.Series(np.array([43725754,56820832]), index=['7/16~8/16','8/16~9/13'])
plt.figure(figsize=(8,5))
plt.suptitle('Sales from corona-related incidents',fontsize=15)
plt.subplot(1,2,1)
plt.title('Disaster support money')
plt.bar(pos_givemoney.index,pos_givemoney)
plt.yticks([0, 10000000, 20000000,30000000,40000000,50000000])
plt.xlabel('day')
plt.ylabel('Ten million won')

plt.subplot(1,2,2)
plt.title('Gwanghwamun protests')
plt.bar(pos_Gwanghwamun.index,pos_Gwanghwamun)
plt.yticks([0, 10000000, 20000000,30000000,40000000,50000000])
plt.xlabel('day')
plt.ylabel('Ten million won')
plt.show()