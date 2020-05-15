#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
num1 = 0
num2 = 1
num3 = 0

if 0<= n <=20: pass
    
else:
    print("n은 0보다 크거나 20보다 작은 자연수이다")
    
    
for i in range(1, n-1):
    num3 = num1 + num2
    num1 = num2
    num2 = num3

print(num3)
    

