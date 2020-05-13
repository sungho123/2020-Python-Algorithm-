while True:
    try :
        n = int(input("0~20 사이의 정수를 입력하시오 : "))
        
        if n < 0 :        
            print("0보다 작을 수 없습니다.")
        elif n >= 20 :        
            print("20보다 작거나 같은 자연수를 입력하세요.")
        else :
            break
    except :
        print("정수만 입력하세요")

x1 = 0
x2 = 1

for i in range(1,n):
    tmp = x2
    x2 += x1
    x1 = tmp
print(x2)

