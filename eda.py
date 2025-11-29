import seaborn as sns
import matplotlib.pyplot as plt


def plot_eda(df):
plt.figure(figsize=(15,10))


plt.subplot(2,2,1)
sns.scatterplot(x='area', y='price', data=df)
plt.title('Area vs Price')


plt.subplot(2,2,2)
sns.scatterplot(x='bedrooms', y='price', data=df)
plt.title('Bedrooms vs Price')


plt.subplot(2,2,3)
sns.scatterplot(x='mainroad', y='price', data=df)
plt.title('Mainroad vs Price')


plt.tight_layout()
plt.show()
