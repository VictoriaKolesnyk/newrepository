from random import randint
l = [randint(1, 100) for i in range(10)]
print(l)
k = int(input('введите число от 0 до 9  '))
for i in range(k, len(l)-1):
    l[i] = l[i+1]
l.pop(len(l)-1)
for i in range(len(l)):
    print(l[i], ',', end=' ')
