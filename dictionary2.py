a = {}
d = ('бабочки полет будит тихую поляну в солнечных лучах'+' старый пруд прыгнула лягушка всплеск в тишине')
c = d.split()
for word in c:
    a[word] = a.get(word, 0) + 1
print(a)
max_value = max(list(a.values()))
w = ''
for key, value in a.items():
    if value == max_value:
        w = key

print(' чаще всего встречается слово : ', w, '\n','всего в тексте : ', max_value)