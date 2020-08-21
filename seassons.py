def season(a):
    if a == 1 or a == 2 or a == 12:
        return "это зима"
    elif a == 3 or a == 4 or a == 5:
        return "это весна"
    elif a == 6 or a == 7 or a == 8:
        return "это лето"
    elif a == 9 or a == 10 or a == 11:
        return "это осень"
    else:
        return "Такого месяца нет"
a = int(input('введите месяц года   '))
print(season(a))
