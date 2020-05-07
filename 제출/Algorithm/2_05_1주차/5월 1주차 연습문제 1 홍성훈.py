while True:
    try :
        n = int(input("0~99 사이의 정수를 입력하시오 : "))
        
        if n > 99 :        
            print("99보다 클 수 없습니다.")
        elif n < 0 :        
            print("0보다 작을 수 없습니다.")
        else :
            break
    except :
        print("숫자만 입력하세요")
    
tmp = n #임시변수
cnt = 0 #사이클 수 변수
while True:
    #오른쪽 자리수(1의자리) 수를 10의 자리로 + (10의자리수 + 1의자리)의  1의 자리수    
    tmp = (tmp%10)*10 + (tmp//10 + tmp%10)%10     
    #print(tmp)
    cnt +=1 #사이클증가
    if n==tmp: #처음 입력한 숫자와 같아지면 break
        break
    
print(n,"사이클의 길이 :", cnt)
