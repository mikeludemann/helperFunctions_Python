def numberToRoman(self, number):
    digits = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    symbolRoman = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    romanNumber = ''
    i = 0
    while number > 0:
        for _ in range(number // digits[i]):
            romanNumber += symbolRoman[i]
            number -= digits[i]
        i += 1
    return romanNumber
