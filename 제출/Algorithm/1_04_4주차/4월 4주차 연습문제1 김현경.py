
a = int(input("세자리수1:"))
b = int(input("세자리수2:"))

str_a = str(a)
str_b = str(b)

l_a = list(str_a)
l_b = list(str_b)

r_a = "".join(reversed(l_a))
r_b = "".join(reversed(l_b))

sum_tot = 0
sum_tmp = 0
sum = 0
sum1 = 0
sum2 = 0
sum3 = 0

for i in range(len(r_b)):
    for j in range(len(r_a)):
        int_a = int(r_a[j])
        int_b = int(r_b[i])
        sum_tmp = (pow(10, j) * int_a *int_b)
        sum = sum + sum_tmp

    if i == 0:
        sum1 = sum1 + sum
        print('(3) :', sum1)
    elif i == 1:
        sum2 = sum2 + sum
        print('(4) :', sum2)
    elif i == 2:
        sum3 = sum3 + sum
        print('(5) :', sum3)

    sum = 0
    sum_tmp = 0

    sum_tot = sum1 + sum2*10 + sum3*100

print('(6) :', sum_tot)
