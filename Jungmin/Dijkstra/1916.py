import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
check = [1] * (N+1)
dist = [float('inf')] * (N+1)
dij = [[float('inf')] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dij[i][i] = 0

for i in range(M):
    start, end, cost = map(int, input().split(' '))
    dij[start][end] = min(cost, dij[start][end])

_start, _end = map(int, input().split(' '))

check[_start] = 0
dist[_start] = 0
while sum(check) != 1:
    for i in range(len(dij[_start])):
        if i != 0:
            if dist[i] == float('inf') and dij[_start][i] != float('inf'):
                dist[i] = dist[_start] + dij[_start][i]

            elif dist[i] != float('inf') and dist[_start] + dij[_start][i] < dist[i]:
                dist[i] = dist[_start] + dij[_start][i]

    _next = [-1, float('inf')]
    for i in range(1, N+1):
        if check[i] == 1 and dist[i] < _next[-1]:
            _next = [i, dist[i]]

    if _next[0] == -1:
        break

    _start = _next[0]
    check[_start] = 0

print(dist[_end])