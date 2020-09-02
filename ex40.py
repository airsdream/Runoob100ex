import random
a = []

#随机生成10位以内整数
n = int(random.random()*10)

#生成随机内容，随机长度的列表
for i in range(n):
    x = int(random.random() * 1000)
    a.append(x)
print(a)

N = len(a)

#逆序列表
for i in range(int(N / 2)):
    a[i],a[N - i - 1] = a[N - i - 1],a[i]
print(a)