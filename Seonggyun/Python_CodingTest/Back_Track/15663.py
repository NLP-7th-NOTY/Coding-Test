import sys

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    visited = [False] * N
    combination = []
    combination_set = set()
    
    def back_track(depth):
        if depth == M:
            comb_tuple = tuple(combination)
            if comb_tuple not in combination_set:
                combination_set.add(comb_tuple)
                print(*combination)
            return
            
        for index in range(len(num_list)):
            if not visited[index]:
                visited[index] = True
                combination.append(num_list[index])
                back_track(depth + 1)
                combination.pop()
                visited[index] = False
    
    back_track(0)
            

if __name__ == "__main__":
    main()
    
    
    
# 다른 방식 (라이브러리 활용)
import sys
from itertools import permutations

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    
    combinations = permutations(num_list, M)
    previous = set()
    
    for combination in combinations:
        if combination not in previous:
            print(*combination)
            previous.add(combination)


if __name__ == "__main__":
    main()