import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

T = int(sys.stdin.readline().strip())


directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dfs(plant: list, x: int, y: int) -> None:
    plant[x][y] = False
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < len(plant)) and (0 <= ny < len(plant[0])) and plant[nx][ny]: 
            dfs(plant, nx, ny)
    
    


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    plant = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        plant[y][x] = True
    worm = 0
    for i in range(N):
        for j in range(M):
            if plant[i][j]:
                dfs(plant, i, j)
                worm += 1
    print(worm)
                