def recursiveListSum(list):
    total = 0
    for element in list:
        if type(element) == type([]):
            total = total + recursiveListSum(element)
        else:
            total = total + element
    return total
