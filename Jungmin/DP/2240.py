T, W = map(int, input().split())
arr = []
pos = 1
move_cnt = 0
for i in range(T):
    arr.append(int(input()))

def inv(pos):
    return 1 if pos == 0 else 0

dp = [[[0, 0] for _ in range(W)] for _ in range(T+1)]

for i in range(1, T+1):
    if arr[i-1] == pos:
        dp[i][move_cnt][pos] = dp[i-1][move_cnt][pos] + 1

    else:
        dp[i][move_cnt][pos] = dp[i-1][move_cnt][pos]
        dp[i][move_cnt+1][inv(pos)] = dp[i-1][move_cnt][pos] + 1