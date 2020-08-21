def arithmetic(arg1, arg2, arg3):
    if arg3 == '+':
        return arg1 + arg2
    elif arg3 == '-':
        return arg1 - arg2
    elif arg3 == '*':
        return arg1 * arg2
    elif arg3 == '/':
        return arg1 / arg2
    else:
        return  "Неизвестная операция"
arg1 = int(input('введите первое число:  '))
arg2 = int(input('введите второе число:  '))
arg3 = input('желаемая операция: ')
print(arithmetic(arg1, arg2, arg3))
