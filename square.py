def square(a):
    p = 4 * a
    s = a ** 2
    diag = a * 4 ** (1 / 2)
    return p, s, diag

    print(p, s, diag)


a = int(input('введите число  '))
print(square(a))