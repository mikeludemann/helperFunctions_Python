x = (41, 62, 32, 88, 43, 11) 
print(x)

x = x + (9,)
print(x)

x = x[:3] + (25, 55, 75)
print(x)

cx = list(x) 

cx.append(30)
cx.insert(0,111)
x = tuple(cx)
print(x)