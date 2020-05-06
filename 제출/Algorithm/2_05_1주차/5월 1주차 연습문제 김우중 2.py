a = int(input())
b = 2*a - 1
c = 2*a - 1
i = 0
over = 0 # 반전

for i in range(0,b):
    if over == 0:
        for k in range(0, i):
            print(' ', end='')
        for j in range(0,c):
            print('*', end='')
        print()
        c = c - 2
        if c <= 0 :
            over = 1
            c = c + 4
    elif over == 1:
        for k in range(0,b-i-1):
            print(' ', end='')
        for j in range(0,c):
            print('*', end='')
        print()
        c = c + 2
