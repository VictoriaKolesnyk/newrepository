n = int(input("введите число:  "))
i = 1
print(n, end=" ")
for i in range(n):
    if i**2 <= n:
        print( i**2, end=" ")

