def isPalindrome(string):
    positionLeft = 0
    positionRight = len(string) - 1

    while positionRight >= positionLeft:
        if not string[positionLeft] == string[positionRight]:
            return False
        positionLeft += 1
        positionRight -= 1
    return True
