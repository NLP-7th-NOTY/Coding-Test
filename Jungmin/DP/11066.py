T = int(input())
res = []

def obj(K, arr):
    sum_arr = [arr[0]]
    for elem in arr[1:]:
        sum_arr.append(sum_arr[-1] + elem)

    dp = [[float('inf') for _ in range(K)] for _ in range(K)]

    for i in range(K):
        dp[i][i] = 0

    for l in range(1, K):
        for i in range(K-l):
            for j in range(i, K-l):
                dp[i][i+l] = min(dp[i][i+l], dp[i][j]+dp[j+1][i+l]+sum_arr[i+l]-sum_arr[i])


for i in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    res.append(obj(K, arr))

for elem in res:
    print(elem)