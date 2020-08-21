sum = 0
n = 1
i = 0
even = 0
odd = 0
my_min = 2
my_max = 1
while n != 0:
    i +=1
    n = int(input("введите число "))
    sum += n

    if n != 0 and n < my_min:
        my_min = n
    if n > my_max:
        my_max = n

    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("максимальне значение", my_max, "минимальное значение", my_min)
print("нечетные :", odd, "четные :", even - 1)
print("количество цифр", i - 1, "сумма", sum, "среднее арифметическое", sum / (i - 1))
