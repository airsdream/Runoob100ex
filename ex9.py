import time

t = int(input('倒计时（秒）：'))

for i in range(1,t+1):
    print(t+1-i)
    time.sleep(1)
print('倒计时%d秒结束'%t)