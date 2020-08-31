import time
import datetime

count = 0

while 1:
    count += 1
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),end='  ')
    print('count =',count)
    time.sleep(0.01)
