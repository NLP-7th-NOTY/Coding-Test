import sys

n, k = map(int, sys.stdin.readline().strip().split())

n_iter = 1
k_iter = 1
n_k_iter = 1

for _ in range(2, n+1):
    n_iter *= _

for _ in range(2, k+1):
    k_iter *= _

for _ in range(2, (n-k) + 1):
    n_k_iter *= _
    
answer = n_iter/(k_iter*n_k_iter)

print(int(answer))