class py_solution:
    def romanToNumber(self, symbol):
        symbolRoman = {'I': 1, 'V': 5, 'X': 10,
                       'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        digits = 0
        for i in range(len(symbol)):
            if i > 0 and symbolRoman[symbol[i]] > symbolRoman[symbol[i - 1]]:
                digits += symbolRoman[symbol[i]] - \
                    2 * symbolRoman[symbol[i - 1]]
            else:
                digits += symbolRoman[symbol[i]]
        return digits
