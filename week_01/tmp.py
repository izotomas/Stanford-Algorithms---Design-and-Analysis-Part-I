inp = open('IntegerArray.txt','r')
L = inp.readlines()


for i in range(len(L)):
    L[i] = int(L[i])

print type(L[0])
print len(L)
for i in range(5):
    print L[i]
