import pandas as pd

df = pd.read_json("./extras/04_data.json");

print(df)
print(df.to_string())

print(df.info())