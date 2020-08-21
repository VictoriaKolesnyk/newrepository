l = []
from random import randint
l = [randint(1,100) for i in range(10)]
print(l)
k = int(input('введите индекс числа "k"  '))
c = int(input('введите число "С " '))
l.append(0)
for i in range(len(l)-1, k, -1):
    l[i] = l[i-1]
    l[k] = c
l.pop(k)
print(l)


