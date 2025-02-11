import sys
from collections import deque


def find_min_time(N, K):
    if N == K:
        return 0 
    
    MAX = 100000
    visited = [-1] * (MAX + 1)
    queue = deque([N])
    visited[N] = 0 # 시작 위치에 대해 방문 처리
    
    while queue:
        x = queue.popleft()
        
        for next_x in (x - 1, x + 1, x * 2):
            if 0 <= next_x <= MAX and visited[next_x] == -1:
                visited[next_x] = visited[x] + 1
                if next_x == K:
                    return visited[next_x]
                queue.append(next_x)
    
    return -1

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().rstrip().split())
    print(find_min_time(N, K))