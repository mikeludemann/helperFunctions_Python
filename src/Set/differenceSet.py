first = set(["green", "blue", "red", "purple"])
second = set(["blue", "yellow", "green"])

result = first | second

print(result)

firstResult = first - result
secondResult = second - result

print(firstResult)
print(secondResult)