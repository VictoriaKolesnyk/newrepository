from random import randint
l= [randint(1, 100) for i in range(1,5)]
print(l*2)
for i in range(len(l)):
    if l[i] == i:
        l[i] +=1
    else:
        continue
print(l[i], l.count(l[i]))
print()


