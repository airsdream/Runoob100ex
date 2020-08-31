import random

a = []

n = int(input('How many nums do you want:'))

for i in range(n):
    a.append(random.randint(0,100))

b = a[:]
print('a list is',a)
print('b list is',b)