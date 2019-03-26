first = set(["apple", "mango"])
second = set(["mango", "orange"])
third = set(["mango"])

issuperset = first >= second
print(issuperset)
issuperset = first >= third
print(issuperset)