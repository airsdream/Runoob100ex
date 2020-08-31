from math import sqrt

count = 0

def judgement (num):
    max = int(sqrt(num+1))
    for i in range(2,max+1):
        if num % i == 0:
            judge = 0
            break
        else:
            judge = 1
    return judge

for num in range(101,201):
    judge = judgement(num)
    if judge == 1:
        print(num,end=' ')
        count += 1
        print('No.%d'%count)

print('Total：',count)
