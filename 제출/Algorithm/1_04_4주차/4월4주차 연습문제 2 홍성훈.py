i = 1
a = []  #점수를 리스트변수로 순서대로 저장
#a = [10, 65, 100, 30, 95]
sum1 = 0 #합계변수

n = 5 # 인원수 변수
while i <= n : #인원수 만큼 반복
    print(str(i),"번째 학생의 점수를 입력하세요 : ")

    try :
        tmp = int(input()) #점수 입력 
        #조건에 따라 입력된 점수 유효성 검증하여 유효한 점수만 저장
        if tmp > 100 :        
            print("100보다 클 수 없습니다.")
        elif tmp < 0 :        
            print("0보다 작을 수 없습니다.")
        elif (tmp%5) != 0:
            print("5점단위로 입력하세요")
        else :
            a.append(tmp) #입력된 점수를 리스트변수에 저장
            i+=1
    except :
        print("숫자만 입력하세요")
 

for a1 in a: #리스트 변수 반복
    if a1<40: #40보다 작은경우 40으로 합산
        sum1 +=40
    else:     #40보다 크거나 같은 경우 원점수로 합산
        sum1 +=a1

print()
print("평균점수 : ",int(sum1/len(a)))#리스트변수의 갯수로 합계를 나눠 평균 계산
