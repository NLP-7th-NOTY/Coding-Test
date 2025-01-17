import sys

A, B = map(int, sys.stdin.readline().strip().split())

# 유클리드 호제법
matmul_AB = A * B

def gcd(A, B):
    while B:
        A, B = B, A % B
    return A

GCD = gcd(A, B)

LCM = int(matmul_AB / GCD)

print(GCD, LCM)