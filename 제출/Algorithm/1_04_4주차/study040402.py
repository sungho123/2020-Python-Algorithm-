score = []

for i in range(0, 5):
    score.append(int(input()))

result = 0

for i in score:
    if i < 40:
        i = 40
    result += i

result = int(result / len(score))

print(result)