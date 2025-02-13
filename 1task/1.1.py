t = ([x for x in range(112) if x ** 2 % 3 == 0 and x ** 2 % 4 == 0 and x ** 2 % 8 != 0 and x ** 2 < 12345])
print(t)