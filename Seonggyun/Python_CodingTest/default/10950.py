number = int(input())

import sys

for _ in range(number):
    a, b = map(int,sys.stdin.readline().strip().split())
    print(a+b)