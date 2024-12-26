N, M = map(int, input().split())
arr = list(map(int, input().split()))
mapper, tot = [0]*(M+1), 0

for elem in arr:
    tot += elem
    mapper[tot % M] += 1

print(sum(x*(x-1)//2 for x in mapper)+mapper[0])