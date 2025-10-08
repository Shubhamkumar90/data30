import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# print(sns.get_dataset_names())
tips=sns.load_dataset('tips')
print(tips[tips.day=='Thur']['tip'].sum())
# print(tips.groupby('day').count())
sns.boxplot(x='day',y='tip',data=tips)
plt.title('Distribution of Tips by Day')
plt.yticks(np.arange(1,11,1))
plt.xlabel('Day')
plt.ylabel('tips')
plt.show()