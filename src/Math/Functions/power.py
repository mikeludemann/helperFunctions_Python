def power(basis, exponent):
    if exponent == 0:
        return 1
    elif basis == 0:
        return 0
    elif exponent == 1:
        return basis
    else:
        return basis*power(basis, exponent-1)
