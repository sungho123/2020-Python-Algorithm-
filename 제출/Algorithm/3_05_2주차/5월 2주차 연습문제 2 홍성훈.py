"""
해당 문제 풀이는 실패해서 "하노이의 탑 알고리즘"으로 구느님께 여쭤본 결과입니다.
함수의 재귀를 이용한 방법과 비재귀로 While문으로 하는 방법이 있습니다.
"""

# 함수 재귀를 이용
# n개의 원반을 from 에서 by를 거쳐 to로 옮긴다.
def hanoi(n, f, by, t, a):
    if (n == 1):
        a.append([f,t])
    else:
        hanoi(n - 1, f, t, by, a)     # 1번 N-1개의 원반을 기둥3을 거쳐 2로 옮긴다.
        a.append([f,t])               # 2번 기둥 1에서 1개의 원반을 기둥 3으롱 롬긴다.
        hanoi(n - 1, by, f, t, a)     # 3번 기둥 2에서 N-1개의 원반을 기둥 3으로 옮긴다.

while True:
    try :
        n = int(input("1~20 사이의 정수를 입력하시오 : "))
        
        if n < 1 :        
            print("1보다 작을 수 없습니다.")
        elif n > 20 :        
            print("20보다 클 수 없습니다.")
        else :
            break
    except :
        print("정수만 입력하세요")

result = []
hanoi(n, 1, 2, 3, result)
print("옮긴 횟수 : ", len(result))
for a1 in result:
    print(a1[0],"에서",a1[1],"로(으로) 이동")


# 비재귀
def hanoi2 (n, f, by, t, a) :
    arr = []
    temp = 1
    while (temp > 0) :
        while (n >1) :
            arr.append(n)
            arr.append(f)
            arr.append(by)
            arr.append(t)
            n -=1
            arr.append(t)
            t = by
            by = arr.pop()
            
        a.append([f, t]);
        
        if (len(arr) -1 > 0) :
            t = arr.pop()
            by = arr.pop()
            f = arr.pop()
            n = arr.pop();
            a.append([f, t])
            n -=1
            arr.append(f)
            f = by
            by = arr.pop()
    
        else :
            temp = 0

result = []
hanoi2(n, 1, 2, 3, result)
print("옮긴 횟수 : ", len(result))
for a1 in result:
    print(a1[0],"에서",a1[1],"로(으로) 이동")
    
