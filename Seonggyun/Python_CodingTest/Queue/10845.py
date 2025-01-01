import sys
from collections import deque

num = int(input())
dq = deque()

for _ in range(num):
    order = list(sys.stdin.readline().strip().split())
    if len(order) == 1:
        if order[0] == 'pop':
            if len(dq) == 0:
                print(-1)
            else:
                result = dq.popleft()
                print(result)
        
        elif order[0] == 'size':
            print(len(dq))
        
        elif order[0] == 'empty':
            print(int(len(dq) == 0))
            
        elif order[0] == 'front':
            if len(dq) == 0:
                print(-1)
            else:
                print(dq[0])
        
        elif order[0] == 'back':
            if len(dq) == 0:
                print(-1)
            else:
                print(dq[-1])
    
    else:
        dq.append(int(order[1]))
        
    
    
    