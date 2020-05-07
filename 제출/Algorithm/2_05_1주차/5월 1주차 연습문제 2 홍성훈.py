while True:
    try :
        n = int(input("1~100 사이의 정수를 입력하시오 : "))
        
        if n > 100 :        
            print("100보다 클 수 없습니다.")
        elif n < 1 :        
            print("1보다 작을 수 없습니다.")
        else :
            break
    except :
        print("숫자만 입력하세요")

l = 2*n-1 #출력 라인수 계산
cnt = 0

for i in range(0,l): #라인 수만큼 반복
    star = ""
    if i < n: #반복의 중간만큼 역삼각형으로 만듦
        for j in range(0,l-i):#라인 반복될수 "*"의 반복수 줄여 역삼각형을 만듦
            if i<=j:
                star += "*"
            else:
                star += " "
    else: #반복이 중가 이후로 삼각형으로 만듦
        for j in range(0,i+1):#라인 반복될수 "*"의 반복수 늘려 삼각형을 만듦
            if l-i>j+1:
                star += " "
            else:
                star += "*"
    print(star,i)
