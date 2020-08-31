last = 1
for i in range(9,0,-1):
    early = (last + 1) * 2
    last = early
print(early)