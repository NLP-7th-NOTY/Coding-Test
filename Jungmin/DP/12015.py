N = int(input())
arr = list(map(int, input().split()))
dp = []

def b_search(dp, elem):
    start, end = 0, len(dp)-1
    while start < end:
        mid = (start+end)//2
        if dp[mid] < elem:
            start = mid + 1
        else:
            end = mid

    return start

for elem in arr:
    if not dp or (dp and dp[-1] < elem):
        dp.append(elem)

    else:
        idx = b_search(dp, elem)
        dp[idx] = elem

print(len(dp))
