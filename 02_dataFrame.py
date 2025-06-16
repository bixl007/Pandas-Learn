import pandas as pd

myDataset = {
    'cars': ["Ford", "BMW", "Bugatti"],
    'Price': [2000000, 500000, 1200000]
}

df = pd.DataFrame(myDataset)
print(df)
print(df.loc[[0,1]])

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print(df.loc["day2"])