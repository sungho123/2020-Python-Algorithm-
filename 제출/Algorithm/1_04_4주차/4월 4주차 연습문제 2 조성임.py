sum = 0
cnt = 5

while cnt > 0:

    jumsu = int(input("학생점수를 입력하세요 : "))

    if jumsu >= 40:
        sum += jumsu
    else:
        sum += 40
    cnt -= 1

print("평균: " , sum/5)
