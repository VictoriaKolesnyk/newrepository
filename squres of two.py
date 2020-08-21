n = int(input("введите число  "))
i = 1
print (n, end=" ")
while n >= 1:
    n = n // 2
    i += 1
print(i - 2,   2**(i-2),   "2**",i - 2,"=",2**(i-2))