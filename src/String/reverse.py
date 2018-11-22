def reverse(string):
    rev = ''
    index = len(string)
    while index > 0:
        rev += string[index - 1]
        index = index - 1
    return rev
