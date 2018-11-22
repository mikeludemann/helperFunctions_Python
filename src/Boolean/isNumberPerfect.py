def isNumberPerfect(number):
    sum = 0
    for x in range(1, number):
        if number % x == 0:
            sum += x
    return sum == number
