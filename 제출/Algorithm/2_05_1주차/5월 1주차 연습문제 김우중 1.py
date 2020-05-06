n = input()
a = n
i = 0


if len(a) == 1:
    a = '0' + a
    n = a

while True:

    b = int(a[0]) + int(a[1])
    b = str(b)
    b = a[-1] + b[-1]
    a = b
    i = i + 1

    # if i < 20:
    #     continue
    # break

    if n != a:
        continue
    break

print(i)
