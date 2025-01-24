import sys
from collections import defaultdict

T = int(sys.stdin.readline().strip())






for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    cabbage_plant = defaultdict([0]*N)
    
    
    