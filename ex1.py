
total = 0

for num1 in range(1,5):
    for num2 in range(1,5):
        for num3 in range(1,5):
            if (num1 != num2) and (num2 != num3) and (num3 !=num1):
                print(num1,num2,num3)
                total += 1
print("sum = ",total)