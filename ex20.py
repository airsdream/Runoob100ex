tour = []
height = []
Sn = 0
reheight = 0

def totaltour (n):
    Sn = hei
    tour.append(Sn)
    for i in range(n):
        tour.append(Sn)
        Sn = Sn / 2
    return

def rejump (n):
    reheight = hei
    for i in range(n):
        reheight = reheight / 2
        height.append(reheight)
    return

hei = int(input('起始高度：'))
tim = int(input('第几次：'))

totaltour(tim)
rejump(tim)

print('总高度：{0}'.format(sum(tour)))
print('第%d次反弹高度:%f'%(tim,height[tim-1]))