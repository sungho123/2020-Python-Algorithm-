import numpy as np

num1 = int(input())  #(1) - 입력되는 세 자리의 수 
num2 = int(input())  #(2) - 입력되는 세 자리의 수

num3 = num1*(num2%10)         #(3) - num1 * num2의 일의 자리 수 
num4 = num1*((num2%100)//10), #(4) - num1 * num2의 십의 자리 수
num5 = num1*(num2//100)       #(5) - num1 * num2의 백의 자리 수

num6 = num1*num2              #(6) - num1 * num2

print(num3, num4, num5, num6) #출력
