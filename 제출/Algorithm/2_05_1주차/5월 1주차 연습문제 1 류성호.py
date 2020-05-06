input_num = int(input())  # input 
cnt = 1                   # output

if input_num >= 0 and input_num <=99: #input 조건 
        num = input_num 
        while True:                   #무한 루프 
            first_num = int(num/10)   #십의 자리 수 
            second_num = int(num%10)  #일의 자리 수 
            
            num = int(str(second_num) + str((first_num + second_num)%10)) #first_num+ (first_num+second_num 의 일의 자리 수)
            
            if input_num == num: #원래의 수로 돌아았을 경우
                break
            else: #원래의 수가 아닌 경우
                cnt+=1
else:
    print("0보다 크고 100보다 작은 수를 입력하시오. ")
    
print(cnt)




