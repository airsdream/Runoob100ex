year = int(input('Year:'))
month = int(input('Month:'))
day = int(input('Day:'))
sum = 0

months = [31,29,31,30,31,30,31,31,30,31,30,31]  #闰年每月日数

def leap (year):    #判断闰年函数
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return 1
    else:
        return 0

def legal (year,month,day): #判断日期合法性函数
    if day <= months[month-1]:
        if leap(year) == 0 and month == 2 and day >= 28:
            mark = 0
        else:
            mark = 1
    else:
        mark = 0
    return mark



if legal(year,month,day):
    for i in range(0,month-1):
        sum += months[i]
    sum += day
    if month > 2 and leap(year) != 1:
        sum -= 1
    print('It is the %dth day in this year' % sum)

else:
    print('Ops! %d-%d-%d is an error date'%(year,month,day))



