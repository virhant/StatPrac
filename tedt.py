str = "hello world"
print(str)
print(str, len(str))

str1 = "pin" + ' ' + "code"
print(str1)

arr = [1, 2, "lol"]
print(arr, arr[-1])
arr1 = arr.pop()
print(arr1, arr)

dict = {"cat" : "milka", "dog" : "chelsea"}
print(dict, len(dict))
print(dict["cat"])

t = (1, 1, 3, 4)
print(t, len(t))
t1 = (1)
t2 = (1,)
print(type(t1), type(t2))

mas = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(mas[0][1])