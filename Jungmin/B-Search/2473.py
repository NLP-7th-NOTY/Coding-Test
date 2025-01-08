N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
res = float('inf')
idx = []

for i in range(N-2):
    left = i+1
    right = N-1

    while left < right:
        curr = arr[i]+arr[left]+arr[right]
        if abs(curr) < res:
            res = abs(curr)
            idx = [arr[i], arr[left], arr[right]]

        if curr < 0:
            left += 1

        else:
            right -=1

print(str(idx)[1:-1].replace(',', ''))