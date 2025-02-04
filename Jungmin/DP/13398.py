N = int(input())
arr = list(map(int, input().split()))
dp_0 = [0] * N
dp_1 = [0] * N

dp_1[0], dp_0[0] = arr[0], arr[0]
res = -float('inf') if N > 1 else max(0, arr[0])

for i in range(1, N):
    dp_0[i] = max(dp_0[i-1] + arr[i], arr[i])
    dp_1[i] = max(dp_1[i-1] + arr[i], dp_0[i-1])

res = max(max(dp_0), max(dp_1))
print(res)