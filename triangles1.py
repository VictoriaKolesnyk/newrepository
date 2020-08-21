# rows = int(input(" Введите ширину треугольника   "))
# cols = int(input("введите высоту треугольника   ")
# for i in range(rows):
# print(i, end='\t')
#     for j in range(cols * 2):
#         if(i == rows - 1 or i == abs(cols - j - 1)):
#             print('* ', end='')
#         else:
#             print('  ', end='')
# print()
#
# hight = int(input(" высота треугольника   "))
# for i in range(hight):
#     print(i + 1, end='\t')
# for j in range(hight):
#     if
# i == 0 or j == 0 or j == hight - i - 1:
# print('* ', end='')
# else:
# print('  ', end='')
# print()
#
#
rows = 11
cols = 11
for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (i == j or i == cols - j -1
                or i == rows // 2 or j == cols // 2):
            print('* ', end='')
        else:
            print('  ', end='')
    print()