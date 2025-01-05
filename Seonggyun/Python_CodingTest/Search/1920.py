import sys
from collections import defaultdict

N = int(input())
N_list = list(map(int, sys.stdin.readline().strip().split()))
num_dict = defaultdict(int)

for n in N_list:
    num_dict[n] += 1
    
M = int(input())
M_list = list(map(int, sys.stdin.readline().strip().split()))

for m in M_list:
    if num_dict[m] == 0:
        print(0)
    else:
        print(1)