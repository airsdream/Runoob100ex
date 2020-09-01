from functools import reduce

n = 20
list = []
temp = 1

for i in range(1,n+1):
    for j in range(1,i+1):
        temp = temp * j
    list.append(temp)
    temp = 1

sum = reduce(lambda x, y : x + y, list)

for i in range(n+1):
    print('%d!'%(i+1),end='')
    if i != n :
        print(' + ',end='')
    else:
        print(' = %d'%sum,end='')