import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, E = map(int, input().split())
arr = list(map(int, input().split()) for _ in range(E))
graph = [[] for _ in range(N+1)]
v1, v2 = map(int, input().split())

for elem in arr:
    a, b, c = elem
    graph[a].append([b,c])
    graph[b].append([a,c])

def dij(start, end):
    dp = [float('inf')] * (N+1)
    visited = [0] * (N+1)
    dp[start] = 0
    next = PriorityQueue()

    visited[start] = 1
    while len(visited) != 1:
        for elem in graph[start]:
            b, c = elem
            if dp[b] == float('inf'):
                dp[b] = dp[start] + elem[-1]
                next.put([dp[b], b])

            elif dp[start] + elem[-1] < dp[b]:
                dp[b] = dp[start] + elem[-1]
                next.put([dp[b], b])

        if next.qsize() == 0:
            return dp[end]

        else:
            start = next.get()[-1]
            while visited[start] != 0:
                if next.qsize() == 0:
                    return dp[end]

                start = next.get()[-1]
            visited[start] = 1

    return dp[end]


path1 = dij(1, v1) + dij(v1, v2) + dij(v2, N)
path2 = dij(1, v2) + dij(v2, v1) + dij(v1, N)

print("-1" if min(path1, path2) == float('inf') else min(path1, path2))