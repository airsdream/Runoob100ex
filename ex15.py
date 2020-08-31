score = int(input('Input Score:'))

if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print('Score:%d = Grade:%s'%(score,grade))