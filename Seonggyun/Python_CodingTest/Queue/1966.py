import sys
from collections import deque

num = int(input())


result = 0
answer = []

for _ in range(num):
    N, question = map(int, sys.stdin.readline().strip().split())
    importnesses = list(map(int, sys.stdin.readline().strip().split()))
    
    dq = deque()
    for index, importness in enumerate(importnesses):
        
        dq.append((index, importness))
    
    
    while True:
        current = dq.popleft()
        if any(current[1] < impt for idx, impt in dq):
            dq.append(current)
        else:
            result +=1
            if current[0] == question:
                answer.append(result)
                result = 0
                break
            
for ans in answer:
    print(ans)