#!/usr/bin/env python
# coding: utf-8

# In[ ]:


num = int(input())
cycle = 1

if 0 <= num <= 99:
    chk_num = num
    
    while True:
        first_num = int(chk_num/10)
        second_num = int(chk_num%10)
        
        chk_num = str(second_num) + str((first_num + second_num)&10)
        
        if chk_num == str:
            break
        else:
            cycle +=1
    
    

    
    
else:
    print("입력값은 0과 99 사이의 정수 입니다")
    
print(cycle)

    


# In[ ]:





# In[ ]:




