l1 = {i*2 for i in range(10)}
l2 = {i*3 for i in range(10)}
#print(l1, l2)
#l3 = l1 & l2
#print(l3)
#print(len(l3))
print(l1, l2, len(l1.intersection(l2)))
print(l1,l2, len(l1.symmetric_difference(l2)))