import seaborn as sns
tips = sns.load_dataset("tips")
ax = sns.regplot(x="total_bill", y="tip", data=tips)