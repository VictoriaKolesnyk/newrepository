l1 = [i for i in range(1, 11)]
l1.sort()
print(l1, end='')
print()
from random import randint
l2 = [randint(1, 100) for i in range(10)]
l2.sort()
print(l2)
i = 0
j = 0
l3 = []
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        l3.append(l1[i])
        i += 1
    else:
        l3.append(l2[j])
        j += 1
while j < len(l2):
    l3.append(l2[j])
    j += 1
print(l3)
