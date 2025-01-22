import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]
S, X, Y = map(int, input().split())

dydx = [[-1,0],[1,0],[0,-1],[0,1]]
virus_heap = []

def one_day(arr, virus_heap):
    _next = []

    while virus_heap:
        level, yx = heapq.heappop(virus_heap)
        y, x = yx

        for elem in dydx:
            _y, _x = y+elem[0], x+elem[1]
            if 0 <= _y < N and 0 <= _x < N and arr[_y][_x] == 0:
                arr[_y][_x] = level
                _next.append([_y, _x])

    for elem in _next:
        y, x = elem
        heapq.heappush(virus_heap, [arr[y][x], [y, x]])

    return arr, virus_heap

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            heapq.heappush(virus_heap, [arr[i][j], [i,j]])

for i in range(S):
    arr, virus_heap = one_day(arr, virus_heap)

print(arr[X-1][Y-1])