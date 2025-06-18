import pandas as pd

df = pd.read_csv('./extras/01_data.csv')

print(df.to_string())

print(pd.options.display.max_rows)