import sys
sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
dydx = [[-1,0],[1,0],[0,-1],[0,1]]

def DFS(dp, cord):
    y, x = cord

    if y == N-1 and x == M-1:
        return 1

    tot = 0
    for elem in dydx:
        _y, _x = y+elem[0], x+elem[1]

        if 0 <= _y < N and 0 <= _x < M and arr[y][x] > arr[_y][_x]:
            if dp[_y][_x] == -1:
                tot += DFS(dp, [_y, _x])

            else:
                tot += dp[_y][_x]

    dp[y][x] = tot
    return tot

DFS(dp, [0,0])
print(dp[0][0])