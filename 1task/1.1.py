t = ([x for x in range(112) if x ** 2 % 3 == 0 and x ** 2 % 4 == 0 and x ** 2 % 8 != 0 and x ** 2 < 12345])
print(type(t)) # Это list, а не tuple

t_new = tuple(x for x in range(int(12345**(0.5)) + 1) if x ** 2 % 12 == 0 and x ** 2 % 8 != 0)
print(t_new, type(t_new))
