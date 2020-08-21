number = int(input('введите высоту треугольника   '))
for i in range(number):
    for j in range(number *2):
        if ((j == number - 1 - i or j == number + i - 1 or i == number - 1) and j < number*2-1):
            print('* ', end='')
        else:
            print('  ', end='')
    print()



height = int(input('Введите высоту тругольника: '))
for i in range(height):
    for j in range(height):
        if i <= height:
            if height - i <= j <= height + i:
                print('* ', end='')
            else:
                print(' ',end='')
    print()
print()


height = int(input("введите высоту треугольника   "))
for i in range(height):
    print()
    for j in range(height * 2):
        if i == height - 1 or i == abs(height - j - 1):
            print('* ', end='')
        else:
            print('  ', end='')
print()


height = int(input('Введите высоту ромба: '))
for i in range(height):
    for j in range(height):
        if i <= height // 2:
            if height // 2 - i <= j <= height // 2 + i:
                print('* ', end='')
            else:
                print('  ', end='')
        else:
            if j == height // 2 + i - height + 1 or j == height // 2 - i + height - 1 or j == height // 2:
                print('* ', end='')
            else:
                print('  ', end='')
    print()
print()


height = int(input('Введите высоту ромба: '))
for i in range(height):
    for j in range(height):
        if i <= height // 2:
            if height // 2 - i <= j <= height // 2 + i:
                print('* ', end='')
            else:
                print('  ', end='')
        else:
            if j == height // 2 + i - height + 1 or j == height // 2 - i + height - 1 :
                print('* ', end='')
            else:
                print('  ', end='')
    print()
print()

