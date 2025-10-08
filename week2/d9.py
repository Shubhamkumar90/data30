import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jane'],
    'Class': ['10A', '10B', '10A', '10B', '10A', '10C', None, '10B', '10C', '10A'],
    'Maths': [88, 76, 93, None, 85, 59, 90, 78, 84, 91]
}
df=pd.DataFrame(data)
print(f"Columns that has missing data:\n{df.isna().sum()}\n")
print(f"Rows missing values:\n{df[df.isna().any(axis=1)]}\n")
# df.dropna(inplace=True)
# df.reset_index(inplace=True,drop=True)
cleaned_df=df.dropna().reset_index(drop=True)
print(f"Cleaned DataFrame:\n{cleaned_df.head(8)}\n")
# p=cleaned_df.groupby('Class')['Maths'].mean()
# print(p)
print(f"Average marks in maths of each class:\n{cleaned_df.groupby('Class')['Maths'].mean()}")