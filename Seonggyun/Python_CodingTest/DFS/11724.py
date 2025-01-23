import sys
from collections import defaultdict

sys.setrecursionlimit(5000)
N, M = map(int, sys.stdin.readline().rstrip().split())

graph = defaultdict(list)

# 그래프 생성
for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부 판단 리스트 하나의 줄기가 뻗어나갈때 전부 체크되고 다므 줄기로
# 넘어가면 다시 체크 안 됨. 경우의수에 따른 완전 탐색
# 출발점에서 visited가 안 되어 있는 경우에만 새로운 줄기가 시작하는 것.

visited = defaultdict(bool)

answer = 0

def dfs(start):
    visited[start] = True
    for dot in graph[start]:
        if not visited[dot]:
            dfs(dot)
        
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)