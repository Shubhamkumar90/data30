import numpy as np
from scipy import stats
import seaborn as sns
import pandas as pd
df = sns.load_dataset('iris')

setosa_petal = df[df['species'] == 'setosa']['petal_length'].values
versicolor_petal = df[df['species'] == 'versicolor']['petal_length'].values
print("Setosa Mean:", np.mean(setosa_petal))
print("Versicolor Mean:", np.mean(versicolor_petal))

print("Setosa Std Dev:", np.std(setosa_petal, ddof=1))
print("Versicolor Std Dev:", np.std(versicolor_petal, ddof=1))
t_stat, p_value = stats.ttest_ind(setosa_petal, versicolor_petal)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.5:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")