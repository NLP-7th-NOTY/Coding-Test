import sys
import heapq

num = int(input())

priority_queue = []


for _ in range(num):
    x, y = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(priority_queue, (x, y))
    
while priority_queue:
    x, y = heapq.heappop(priority_queue)
    print(x,y)