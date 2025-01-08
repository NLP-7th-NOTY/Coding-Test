import sys

lines = sys.stdin.readlines()

for line in lines:
    A, B = map(int, line.rstrip().split())
    print(A+B)

