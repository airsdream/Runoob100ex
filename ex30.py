a = int(input('请输入一个数字：'))
x = str(a)
flag = True

for i in range(int(len(x) / 2)):
    if x[i] != x[-i-1]:
        flag = False
        break

if flag :
    print('%d 是一个回文数'%a)
else:
    print('%d 这不是一个回文数'%a)
