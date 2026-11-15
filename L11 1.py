import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()
print(df.head())
print(df.info())

sns.barplot(x= 'day', y='total_bill', hue='sex', data=df)
plt.title('Average Total Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')

sns.countplot(x='day', hue='sex', data=df)
plt.title('Number of Diners per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Spread of Total Bill per Day')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.stripplot(x='day', y='total_bill', data=df, jitter=True)
plt.title('Every Bill Amount per Day (Strip Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.swarmplot(x='day', y='total_bill', data=df)
plt.title('Every Bill Amount per Day (Swarm Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df)
plt.suptitle('Total Bill vs Tip - KDE Joint Plot', y=1.02)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df, kind='kde')
plt.suptitle('Total Bill vs Tip', y=1.02)
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pair Plot - Bill, Tip and Party Size', y=1.02)
plt.show()

sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.lmplot(x='total_bill', y='tip', data=df)
plt.title('Total Bill vs Trend Line')
plt.show()