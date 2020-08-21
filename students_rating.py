from pprint import pprint
text ="""Андрей Говорухин 6 6 1 4 9 9 10 4 8 2 3 8
 Василий Петров 2 9 4 7 6 6 3 6 5 5 2 4
 Гавриил Варфаломеев 10 10 4 10 7 9 4 6 8 1 1 1
 Игнат Тюльпанов 8 1 4 1 1 5 2 5 2 2 10 8
 Илья Муромцев 1 6 4 7 10 9 5 3 7 4 7 2
 Кощей Бессмертный 3 10 1 4 1 8 10 6 2 10 7 4
 Максим Мухин 10 8 9 9 5 8 6 5 7 2 4 10
 Маргарита Мартынова 9 1 5 1 10 10 2 4 4 9 8 10
 Петр Николаев 2 9 5 9 1 2 8 7 8 1 9 1
 Полина Гусева 9 2 8 7 3 9 9 5 1 9 2 6
 Спиридов Тереньтьев 4 7 7 3 10 9 7 2 10 9 8 1
 Станислав Трердолобов 8 1 6 1 4 1 10 8 8 1 8 8"""

names = [name.strip() for name in text.strip('\n').split('\n')]
pprint(names)
counter = 0
summa = 1
for line in names:
    counter += 1
    length_line = len(names)
    for i in range(length_line):
            num = names[:-12]
            summa += num
            if num > 5:
                print("Ученик(ца) у которого средний бал по классу меньше 5:", line)
            break

    s_a = counter // summa
    print("Средний бал по классу:", s_a)

