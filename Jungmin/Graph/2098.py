N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(1 << N)]

for i in range(1, N):
    if graph[i][0]:
        dp[(1<<N)-2][i] = graph[i][0]
    else:
        dp[(1<<N)-2][i] = float('inf')

def DFS(current, prev):
    if dp[current][prev] != -1:
        return dp[current][prev]

    for i in range(1, N):
        if graph[prev][i] and not(current & 1 << i):
            if dp[current][prev] == -1:
                dp[current][prev] = DFS(current | 1 << i, i) + graph[prev][i]

            else:
                dp[current][prev] = min(dp[current][prev], DFS(current | 1 << i, i) + graph[prev][i])

    return dp[current][prev] if dp[current][prev] != -1 else float('inf')

print(DFS(0, 0))