import random
a = []

def fun ():
    for i in range(10):
        x = int(random.random()*1000)
        a.append(x)

    print(a)

    N = len(a)

    for i in range(N - 1):
        min = i
        for j in range(i+1,N):
            if a[min] > a[j] :
                min = j
        a[min],a[i] = a[i],a[min]

    print(a,end='\n\n')
    del a[:]

    return

for i in range(10):
    fun()