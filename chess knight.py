x = int(input("введите исходные данные по оси х__"))
y = int(input("ведите исходные данные по оси y__"))
a = int(input("введите предполагаемую позицию по х__"))
b = int(input("ведите предполагаемую позицию по оси y__"))
if a - x == 2 and b - y == 1 or x - a == 2 and y - b == 1 or a - x == 1 and\
        b - y == 2 or x - a == 1 and y - b == 2 or a - x == 2 and y - b == 1 or a - x == 1 and y - b == 2 or\
        x - a == 1 and b - y == 2 or x - a == 2 and b - y == 1:
    print("да, конь может так ходить")
else:
    print("нет, конь так не ходит")
