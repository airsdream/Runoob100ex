from functools import reduce

Tn = 0
Sn = []

n = int(input('项数 = '))
a = int(input('基本数 = '))

for i in range(n):
    Tn += a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

total = reduce(lambda x , y : x + y , Sn)
print('计算和 =',total)