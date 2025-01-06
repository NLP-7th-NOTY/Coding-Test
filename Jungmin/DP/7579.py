N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
res = float('inf')

dp = [[-1 for _ in range(sum(cost)+1)] for _ in range(N+1)]
dp[0] = [0 for _ in range(sum(cost)+1)]

for i in range(1, N+1):
    m, c = memory[i-1], cost[i-1]
    for j in range(sum(cost)+1):
        if c > j:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j-c] + m, dp[i-1][j])

        if dp[i][j] >= M:
            res = min(res, j)

print(res)