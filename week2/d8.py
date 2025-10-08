import pandas as pd
data=pd.read_csv("data30/week2/students_marks.csv")
print("\t---Data Information---")
print(data.info())
print("\n\t--- Top 5 Rows ---")
print(data.head(5))
print("\n\t--- Summary Statistics ---")
print(data.describe())