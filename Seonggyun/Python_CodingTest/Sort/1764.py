import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

no_hear = set()
no_see = set()


for _ in range(N):
    no_hear.add(sys.stdin.readline().rstrip())

for _ in range(M):
    no_see.add(sys.stdin.readline().rstrip())

answer = no_hear & no_see    
answer = list(answer)
answer.sort()

print(len(answer))
for name in answer:
    print(name)