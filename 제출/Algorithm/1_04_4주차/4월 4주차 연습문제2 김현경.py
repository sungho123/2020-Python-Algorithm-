s1 = int(input(""))
s2 = int(input(""))
s3 = int(input(""))
s4 = int(input(""))
s5 = int(input(""))

score = [s1, s2, s3, s4, s5]

sum = 0

for i in range(len(score)):
    if score[i]  < 40 :
        score[i] = 40

    sum = sum + score[i]

avg = sum / 5

print(avg)


