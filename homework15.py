from random import randint
a = [randint(0, 100) for i in range(20)]
print(a)
b = set(a)
print(b)
print(len(b))
print(len(set(randint(0, 100) for i in range(20))))