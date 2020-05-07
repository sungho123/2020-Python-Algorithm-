ip = input()
cnt = 0

if len(ip) < 2 :
    ip = '0'+ ip
print(ip)

number = ip 
while True :
    cnt += 1
    backnum = number[1]
    num = int(number[0]) + int(number[1])
    if num >= 10 :
        num %= 10
    number = backnum + str(num)
    if ip == number :
        break
print(cnt)
