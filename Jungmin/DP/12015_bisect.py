from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
dp = []

for elem in arr:
    idx = bisect_left(dp, elem)
    if idx == len(dp):
        dp.append(elem)
    else:
        dp[idx] = elem

print(len(dp))