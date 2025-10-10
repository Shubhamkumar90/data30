import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset('iris')

print(f"Iris Data:\n{df.head()}\n")
print(f"Missing data:\n{df.isnull().sum()}")
print(f"Data Description:\n{df.describe()}")
print(f"Species Count:\n{df['species'].value_counts()}")
# sns.countplot(x='species',data=df)
# plt.title("Species")
# plt.show()
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Features")
plt.show()

# plt.figure(figsize=(12, 6))
# for i, feature in enumerate(df.columns[:-1]):
#     plt.subplot(1, 4, i+1)
#     sns.boxplot(x='species', y=feature, data=df)
#     plt.title(feature)
# plt.tight_layout()
# plt.show()
