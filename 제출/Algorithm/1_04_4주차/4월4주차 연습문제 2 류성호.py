import numpy as np

student_score = []                # 학생 점수를 담을 리스트

for i in range(0,5):              # 다섯 명의 학생 점수 입력 
    score = int(input())
    
    if score < 40:                # 40점 보다 작을 경우
        score = 40
    
    student_score.append(score)   # 리스트 추가 
    
print(int(sum(student_score)/5))  # 평균 계산 + 출력
