import pandas as pd

df = pd.read_csv("./extras/05_data.csv")

new_df = df.dropna() # This will remove the rows that contain empty cells
# if we want to change the original dataFrame then use "df.dropna(inplace = True)"
print(new_df.to_string())

df1 = df.fillna(130) # Replace the null value
print(df1.to_string())

df2 = df.fillna({"Calories" : 130})
print(df2.to_string())

'''
.mean() -> for mean
.median() -> for median
.mode() -> for mod
'''

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())

df.dropna(subset=['Date'], inplace = True)
print(df.to_string())