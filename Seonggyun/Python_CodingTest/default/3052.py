answer = []
for _ in range(10):
    number = int(input())
    answer_temp = number % 42
    answer.append(answer_temp)

answer = set(answer)
print(len(answer))