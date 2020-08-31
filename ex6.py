fib = [1,1]

def calcfib(n):
    if n > 2:
        for i in range(2,n):
            new = fib[i-1]+fib[i-2]
            fib.append(new)

n = int(input('Which num of Fibonacci do you want:'))

calcfib(n)

print('Totals nums are:',fib)
print('The num of Fibonacci which you want is :',fib[n-1])

