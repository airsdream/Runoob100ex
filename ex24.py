fib = [1,1]
denominator = [] #分子
molecular = []  #分母
sum = 0

def calcfib(n):
    if n > 2:
        for i in range(2,n):
            new = fib[i-1]+fib[i-2]
            fib.append(new)

n = int(input('How many = '))

calcfib(n+2)

for i in range(0,n):
    denominator.append(fib[i+2])
    molecular.append(fib[i+1])
    sum += denominator[i]/molecular[i]

for i in range(0,n):
    print('%d/%d'%(denominator[i],molecular[i]),end='')
    if i != n-1 :
        print(' + ',end='')
    else:
        print(' = %f'%sum)