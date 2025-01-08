from itertools import combinations
from collections import deque

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.append([-1 for _ in range(M)])
idx = [i for i in range(M)]
dydx = [[-1,0],[1,0],[0,-1],[0,1]]
res = -1
atomic_enemy = list([y,x] for x in range(M) for y in range(N) if arr[y][x] == 1)

def dist(c1, c2):
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])

def BFS(start, queue):
    visited = [[-1 for _ in range(M)] for _ in range(N+1)]
    enemy = [float('inf'), float('inf'), float('inf')]
    while queue:
        y,x,d = queue.popleft()
        visited[y][x] = 1

        if arr[y][x] == 1:
            if d == enemy[-1] and x < enemy[1]:
                enemy = [y, x, d]
            elif d < enemy[-1]:
                enemy = [y, x, d]

        elif enemy[-1] < d:
            continue

        for elem in dydx:
            _y, _x = y+elem[0], x+elem[1]
            dst = dist(start, [_y,_x])

            if 0 <= _y < N and 0 <= _x < M and visited[_y][_x] == -1 and dst <= D:
                queue.append([_y, _x, dst])

    return enemy

comb = list(combinations(idx, 3))
for elem in comb:
    flag = True
    dead = 0
    for idx in elem:
        arr[-1][idx] = 2

    while flag:
        enemy_list = set()
        for j in range(len(arr[-1])):
            if arr[-1][j] == 2:
                enemy = BFS([N, j], deque([[N, j, 0]]))
                if sum(enemy) != float('inf'):
                    enemy_list.add(tuple(enemy))

        for elem in enemy_list:
            y,x,_ = elem
            if arr[y][x] == 1:
                arr[y][x] = 0
                dead += 1

        next = False
        for i in range(N-1, -1, -1):
            for j in range(M):
                if arr[i][j] == 1:
                    if i+1 == N:
                        arr[i][j] = 0

                    elif arr[i+1][j] == 0:
                        arr[i][j] = 0
                        arr[i+1][j] = 1
                        next = True

        flag = next

    res = max(dead, res)
    arr = [[0 for _ in range(M)] for _ in range(N)]

    for elem in atomic_enemy:
        arr[elem[0]][elem[1]] = 1

    arr.append([-1 for _ in range(M)])

print(res)