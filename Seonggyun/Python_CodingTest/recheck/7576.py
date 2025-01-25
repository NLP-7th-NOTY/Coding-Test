import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

tomato_storage = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

tomato = deque()

for n in range(N):
    for m in range(M):
        pick = tomato_storage[n][m]
        if pick == 1:
            tomato.append((n, m))
            
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]


answer  = 0

while tomato:
    x, y = tomato.popleft()
    temp = 0
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < N) and (0 <= ny < M) and (tomato_storage[nx][ny] == 0):
            tomato_storage[nx][ny] = tomato_storage[x][y] + 1
            tomato.append((nx, ny))

for row in tomato_storage:
    for value in row:
        if value == 0:
            print(-1)
            exit()
        answer = max(answer, value)

print(answer - 1)
    
            
    