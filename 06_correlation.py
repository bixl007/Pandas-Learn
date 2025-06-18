import pandas as pd

df = pd.read_csv("./extras/06_data.csv")
print(df.to_string())

print(df.corr()) # used to find out the relationship between each column in the dataset, this funciton ignores non numeric columns