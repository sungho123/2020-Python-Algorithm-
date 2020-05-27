import numpy as np

input_num = int(input("input data :"))

a = 1
b = 2
c = 3

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c, sep = " ")
    else:
        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)
        
print(2**input_num-1)
if(input_num <= 20):
  hanoi(input_num, a, b, c)
        

        
        