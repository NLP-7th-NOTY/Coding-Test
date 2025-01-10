N = int(input())

answer = 1
target = 1
temp = 1

while target < N:
    target += 6*temp
    temp += 1
    answer += 1

print(answer)