from itertools import combinations
from collections import deque

N, M = map(int, input().split())
dydx = [[-1,0],[1,0],[0,-1],[0,1]]
arr = [list(map(int, input().split())) for _ in range(N)]
candidate = [[i, j] for j in range(N) for i in range(N) if arr[i][j]==2]
candidate_ = list(combinations(candidate, M))
n_empty = sum([1 for j in range(N) for i in range(N) if arr[i][j] == 0])
ans = -1

def BFS(queue):
    t_empty = 0
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    res = 0
    while queue:
        y,x,d = queue.popleft()
        visited[y][x] = 0

        for elem in dydx:
            _y, _x = y+elem[0], x+elem[1]

            if 0 <= _y < N and 0 <= _x < N and visited[_y][_x] == -1 and arr[_y][_x] != 1:
                visited[_y][_x] = 0

                if arr[_y][_x] == 0:
                    queue.append([_y,_x,d+1])
                    t_empty += 1

                elif arr[_y][_x] == 2:
                    queue.append([_y,_x,d+1])

        if t_empty == n_empty:
            res = d+1
            break

    return -1 if t_empty != n_empty else res

for elem in candidate_:
    queue = deque([])
    for _data in elem:
        queue.append([_data[0], _data[1], 0])

    res = BFS(queue)
    if res != -1:
        if ans == -1:
            ans = res

        else:
            ans = min(ans, res)

print(-1 if ans == -1 else 0 if n_empty == 0 else ans)