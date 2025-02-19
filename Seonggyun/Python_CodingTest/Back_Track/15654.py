import sys

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    visited = [False] * N
    result = [] 
        
    def back_track(depth):
        if depth == M:
            print(*result)
            return
    
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                result.append(num_list[i])
                back_track(depth + 1)
                result.pop()
                visited[i] = False
    
    back_track(0)
    


if __name__ == "__main__":
    main()
    
    

# 그런데 이거 이미 파이썬에 구현되어 있음
import sys
from itertools import permutations

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
    
    for permutation in permutations(num_list, M):
        print(*permutation)
    

if __name__ == "__main__":
    main()