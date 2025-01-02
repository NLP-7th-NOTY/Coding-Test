import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[1] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dydx = [[-1,0],[1,0],[0,-1],[0,1]]
res = 0
def DFS(y,x):
    if dp[y][x] != 1:
        return dp[y][x]

    for elem in dydx:
        _y, _x = y+elem[0], x+elem[1]
        if 0 <= _y < N and 0 <= _x < N and arr[y][x] < arr[_y][_x]:
            dp[y][x] = max(dp[y][x], DFS(_y, _x) + 1)

    return dp[y][x]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        res = max(res, DFS(i, j))

print(res)