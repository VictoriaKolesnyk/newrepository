f_name = input('Файл: ')
f = open(f_name, 'w')
while True:
    s = input()
    if s == '':
        break
    f.write(s + '\n')
f.close()

