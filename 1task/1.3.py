def count_words(str):
    return {list(str)[i] : str.count(list(str)[i]) for i in range(len(str))}

str = "hello, world!"
print(count_words(str))

A = sum([1/i**2 for i in range(1, 10001)])
B = sum([1/i**2 for i in range(10000, 0, -1)])
print(A, B)