line = int(input('菱形高度='))

#打印上半段
for i in range(1, line+1):
    for j in range(0, line - i):
        print(' ', end='')
    for k in range(0, 2 * i - 1):
        print('*',end='')
    print()

#打印下半段
for i in range(1, line):
    for j in range(0, i):
        print(' ', end='')
    for k in range(0, 2 * (line-i) - 1):
        print('*', end='')
    print()
