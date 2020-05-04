sum = 0
for i in range(0, 5) :
    num = int(input())
    if num <= 40 :
        num = 40
    sum += num

print(sum / (i+1))
