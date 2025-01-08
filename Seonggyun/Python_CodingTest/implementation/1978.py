import sys

N = int(input())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))
answer = 0

for num in num_list:
    target = 0
    for n in range(1, num+1):
        if not (num % n):
            target += 1
        
    if target == 2:
        answer += 1

print(answer)