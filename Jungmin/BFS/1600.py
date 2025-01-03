horse_dydx = [[2,-1],[2,1],[-2,-1],[-2,1],[1,-2],[1,2],[-1,-2],[-1,2]]
monkey_dydx = [[-1,0],[1,0],[0,-1],[0,1]]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
dp = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

def BFS(queue, arr, dp):
    while queue:
        y,x,c,k = queue.pop(0)
        dp[y][x][k] = c

        if k < K:
            for elem in horse_dydx:
                _y, _x = y + elem[0], x + elem[1]
                if 0 <= _y < H and 0 <= _x < W and dp[_y][_x][k+1] == 0 and arr[_y][_x] == 0:
                    dp[_y][_x][k+1] = dp[y][x][k] + 1
                    queue.append([_y, _x, c+1, k+1])

        for elem in monkey_dydx:
            _y, _x = y+elem[0], x+elem[1]
            if 0 <= _y < H and 0 <= _x < W and dp[_y][_x][k] == 0 and arr[_y][_x] == 0:
                dp[_y][_x][k] = dp[y][x][k] + 1
                queue.append([_y, _x, c+1, k])

    return dp

queue = [[0,0,0,0]]
dp = BFS(queue, arr, dp)
res = [i for i in dp[H-1][W-1] if i != 0]
if H == 1 and W == 1:
    print(0)

else:
    print(-1 if not res else min(res))