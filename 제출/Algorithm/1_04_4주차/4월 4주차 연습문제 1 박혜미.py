a = int(input())
b = int(input())

nnn = str(b)[::-1]
ind = 1
mul = 0
sum = 0
for n in nnn :
    mul = int(a) * int(n)
    print( mul )
    mul *= ind
    ind *= 10
    sum += int(mul)

print(sum)
