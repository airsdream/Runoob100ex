def judgement (num):
    i = num // 100
    j = num // 10 % 10
    k = num % 10
    result = i*i*i + j*j*j + k*k*k
    if num == result:
        return 1

for num in range(100,1000):
    if judgement(num) == 1:
        print(num)