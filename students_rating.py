s = open("source.txt", encoding='utf-8')
d = open("destination.txt", 'w')

template = '{surname:<20}{avr:>6}\n'
data = s.readlines()
total_sum = 0
total_cnt = 0
for line in data:
    lst = line.strip('\n').split()
    suma = sum([int(x) for x in lst[2:]])
    total_sum += suma
    cnt = len(lst[2:])
    total_cnt += cnt
    name = lst[1] + ' ' + lst[0][0] + '.'
    avr = round(suma/cnt, 2)
    if avr < 5:
        print(name, avr)

    d.write(
        template.format(
            surname=name,
            avr=avr
        )
    )

print('Average makr:', round(total_sum/total_cnt, 2))
s.close()
d.close()




