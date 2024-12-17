import sys
input = sys.stdin.readline

def bellman_ford(graph, n):
    dist = [0] * (n+1)

    for _ in range(n):
        update = False
        for node in graph:
            for next_node, weight in graph[node]:
                if dist[next_node] > dist[node] + weight:
                    dist[next_node] = dist[node] + weight
                    update = True

        if not update:
            break

    for u in range(1, n+1):
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                return True

    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = {i: [] for i in range(1, N+1)}

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))

    print("YES" if bellman_ford(graph, N) else "NO")