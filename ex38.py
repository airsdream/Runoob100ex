import random

a = []
sum = 0

for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(int(random.random()*100))

for i in range(3):
    print(a[i])
    sum += a[i][i]
print('sum = %d'%sum)

