i = int(input('净利润（万元）：'))

profit = [100,60,40,20,10,0]
percent = [0.01,0.015,0.03,0.05,0.075,0.1]
award = 0

for id in range(0,6):
    if i > profit[id]:
        award += (i - profit[id]) * percent[id]
        i = profit[id]

print('提成奖金（万元）：',award)