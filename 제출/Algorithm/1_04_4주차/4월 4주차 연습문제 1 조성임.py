num01 = input("세자리 정수1 입력해주세요 : ")
num02 = input("세자리 정수2 입력해주세요 : ")

cal = 0
result = 0

for j in range (1,4) :
    a = (int(num02[-1 * j]) * int(num01[-1])) # % 10 나머지
    b = (int(num02[-1 * j]) * int(num01[-2]))  + a // 10 # // 정수몫
    c = (int(num02[-1 * j]) * int(num01[-3]))  + b // 10  # % 10 나머지
    cal = c*100 + b%10*10 + a%10
    print(j , "번째: " ,cal)
    if j == 1:
        result = cal * 1
    elif j == 2:
        result +=  cal * 10
    elif j == 3:
        result += cal * 100

print("결과 값: " , result)

