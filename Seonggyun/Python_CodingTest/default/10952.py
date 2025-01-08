import sys

while True:
    A, B = map(int, sys.stdin.readline().strip().split())
    if not A and not B:
        break
    print(A+B) 