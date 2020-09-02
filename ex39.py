import random
a = []
b = []
mark = -1

class bcolor:
    HighLight = '\033[93m'
    Normal = '\033[0m'

def fun ():
    for i in range(10):
        x = int(random.random()*1000)
        a.append(x)

    print(a)

    N = len(a)
    for i in range(N):
        b.append(a[i])

    for i in range(N - 1):
        min = i
        for j in range(i+1,N):
            if b[min] > b[j] :
                min = j
        b[min],b[i] = b[i],b[min]

    print(b,end='\n\n')

    return

#生成列表并排序
fun()

#生成随机数
insert = int(random.random()*1000)
print('insert number = %d'%insert)

#比较大小并插入列表
for i in range(len(b)):
    if insert >= b[-1]:
        b.append(insert)
        print('insert position = No.%d'%(len(b)))
        mark = len(b)
        break
    if b[i] > insert:
        b.insert(i,insert)
        print('insert position = No.%d' %(i+1))
        mark = i + 1
        break


#打印列表，并高亮插入值
for i in range(len(b)):
    if i == len(b) - 1:
        end = ''
    else:
        end = ','

    if i == mark-1:
        print(bcolor.HighLight + str(b[i]) + bcolor.Normal, end=end)
    else:
        print(str(b[i]),end=end)