import sys

N = int(sys.stdin.readline().rstrip())
P_list = list(map(int, sys.stdin.readline().strip().split()))

P_list.sort()

target = 0
answer = 0

for p in P_list:
    target += p
    answer += target
    
print(answer)