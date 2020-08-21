d = {}
a = ('бабочки полет будит тихую поляну в солнечных лучах')
b = a.split()
print(b)
for word in b:
    d[word] = d.get(word, 0) + 1
    print(d[word], end=' ')


