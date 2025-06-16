import pandas as pd

arr = [1, 4, 5, 2, 9]

mySeries = pd.Series(arr)
print(mySeries)
print(mySeries[0])
print(mySeries[3])

mySer = pd.Series(arr, index = ["a", "b", "c", "d", "e"])
print(mySer)
print(mySer["a"])
print(mySer["e"])

val = pd.Series({"a": 1, "b": 2, "c": 3})
print(val)