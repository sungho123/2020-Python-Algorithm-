a = int(input("0보다 크거나 같고, 99보다 작거나 같은 정수:"))

cnt = 0
orgNum = 0
nextNum1 = 0
nextNum2 = 0

orgNum = a

while 1:
    cnt += 1
    nextNum1 = orgNum % 10
    nextNum2 = orgNum // 10
    orgNum = nextNum1*10 + (( nextNum1 + nextNum2 ) % 10 )
    if a == orgNum :
        break
print(cnt)
