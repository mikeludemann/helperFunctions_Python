def countCamelCaseCharacter(string):
    d = {"UPPERCASE": 0, "LOWERCASE": 0}
    for c in string:
        if c.isupper():
            d["UPPERCASE"] += 1
        elif c.islower():
            d["LOWERCASE"] += 1
        else:
            pass
    print("Upper Case Characters (Count) : ", d["UPPERCASE"])
    print("Lower Case Characters (Count) : ", d["LOWERCASE"])
