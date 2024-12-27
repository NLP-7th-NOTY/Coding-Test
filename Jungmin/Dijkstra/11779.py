import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for i in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e,c])

A, B = map(int, input().split())
path = [float('inf') for _ in range(N+1)]
route = [[] for _ in range(N+1)]
path[A] = 0
queue = [[0, A, [A]]]
while queue:
    c, s, r = heapq.heappop(queue)

    if path[s] < c:
        continue

    for e, c in graph[s]:
        if path[s] + c < path[e]:
            path[e] = path[s] + c
            r.append(e)
            route[e] = list(r)
            heapq.heappush(queue, [path[e], e, route[e]])
            r.pop()

print(f"{path[B]}\n{len(route[B])}\n{str(route[B])[1:-1].replace(',','')}")
