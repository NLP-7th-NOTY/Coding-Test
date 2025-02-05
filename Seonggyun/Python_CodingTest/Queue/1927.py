import sys
import heapq

N = int(sys.stdin.readline().rstrip())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    
    if x != 0:
        heapq.heappush(heap, x)
    
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)