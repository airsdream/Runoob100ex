from math import sqrt

l = []

def judgement (num):
    global res
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0 :
            res = i
            break
        else:
            res = num
    return res

num = int(input('Input:'))
raw = num
x = 1

while x <= num and num > 1:
    x = int(judgement(num))
    l.append(x)
    num = num / x

print(int(raw),'=',end=' ')

for i in range(0,len(l)):
    if i == len(l)-1:
        print(l[i])
    else:
        print(l[i],'* ',end='')
