first = set(["apple", "mango"])
second = set(["mango", "orange"])
third = set(["mango"])

issubset = first <= second
print(issubset)
issubset = first <= third
print(issubset)