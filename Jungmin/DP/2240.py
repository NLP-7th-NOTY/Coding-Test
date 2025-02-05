T, W = map(int, input().split())
arr = []
dp = [[0 for _ in range(W+1)] for _ in range(T+1)]
for i in range(T):
    arr.append(int(input()))

for i in range(1, T+1):
    for j in range(W+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + 1 if arr[i-1] == 1 else dp[i-1][j]

        else:
            temp = list(zip(*dp))[j - 1]
            if j % 2 == 1:
                # current on tree 2
                dp[i][j] = max(max(temp[:i]) + 1, dp[i-1][j] + (1 if arr[i-1] == 2 else 0))

            else:
                # current on tree 1
                dp[i][j] = max(max(temp[:i]) + 1, dp[i-1][j] + (1 if arr[i-1] == 1 else 0))

print(max(dp[-1]))