from collections import deque
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
depth = [[float('inf') for _ in range(C)] for _ in range(R)]
dydx = [[-1,0],[1,0],[0,-1],[0,1]]
fire_deque = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'F':
            fire_deque.append([i,j,0])
        elif arr[i][j] == 'J':
            jy, jx = i, j
            depth[jy][jx] = -1

def BFS(deque, depth):
    visited = [[0 for _ in range(C)] for _ in range(R)]
    while deque:
        y, x, day = deque.popleft()
        visited[y][x] = 1

        for elem in dydx:
            new_y, new_x = y+elem[0], x+elem[1]
            if 0 <= new_y < R and 0 <= new_x < C and arr[new_y][new_x] == '.' and visited[new_y][new_x] == 0:
                visited[new_y][new_x] = 1
                depth[new_y][new_x] = min(depth[new_y][new_x], day+1)
                deque.append([new_y, new_x, day+1])

    return depth

def BFS2(deque, depth):
    visited = [[0 for _ in range(C)] for _ in range(R)]
    while deque:
        y, x, day = deque.popleft()
        visited[y][x] = 1

        if x == 0 or x == C-1 or y == 0 or y == R-1:
            return day

        for elem in dydx:
            new_y, new_x = y+elem[0], x+elem[1]
            if 0 <= new_y < R and 0 <= new_x < C and depth != float('inf') and day < depth[new_y][new_x] and visited[new_y][new_x] == 0 and arr[new_y][new_x] == '.':
                visited[new_y][new_x] = 1
                deque.append([new_y, new_x, day+1])

    return -1

depth = BFS(fire_deque, depth)
ret = BFS2(deque([[jy,jx,1]]), depth)
print("IMPOSSIBLE" if ret == -1 else ret)