import sys
import heapq


def dijkstra(start, graph, N):
    """ 다익스트라 알고리즘을 사용하여 start 노드에서 모든 노드까지의 최단 거리 계산 """
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0
    
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_dist, village = heapq.heappop(pq)
        if current_dist > dist[village]:
            continue
        
        for arrive, far in graph[village]:
            if dist[arrive] > current_dist + far:
                dist[arrive] = current_dist + far
                heapq.heappush(pq, (dist[arrive], arrive))
                
    return dist


<<<<<<< Updated upstream
def main():
    N, M, X = map(int, sys.stdin.readline().rstrip().split())
    
    # 정방향 및 역방향 그래프 생성
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        start, arrive, far = map(int, sys.stdin.readline().rstrip().split())
        graph[start].append((arrive, far))       # 정방향 그래프
        reverse_graph[arrive].append((start, far))  # 역방향 그래프

    # 정방향 다익스트라 (각 학생 → X)
    to_X_distances = dijkstra(X, reverse_graph, N)
    
    # 역방향 다익스트라 (X → 각 학생)
    from_X_distances = dijkstra(X, graph, N)
    
    # 각 학생의 왕복 최단 거리 계산 후 최댓값 찾기
    max_time = max(to_X_distances[i] + from_X_distances[i] for i in range(1, N + 1))
    
    print(max_time)
=======
def cost_list(cost_graph, n, INF):
    for i in range(1, n + 1):  # 경유지
        for j in range(1, n + 1):  # 출발지
            for k in range(1, n + 1):  # 도착점
                if cost_graph[j][k] > cost_graph[j][i] + cost_graph[i][k]:
                    cost_graph[j][k] = cost_graph[j][i] + cost_graph[i][k]
>>>>>>> Stashed changes

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if cost_graph[i][j] == INF:
                cost_graph[i][j] = 0

    return cost_graph


def main():
    n = int(input())
    m = int(input())
    INF = float('inf')

    cost_graph = [[INF]* (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        start, arrive, cost = map(int, sys.stdin.readline().rstrip().split())
        cost_graph[start][arrive] = min(cost_graph[start][arrive], cost)


    answers = cost_list(cost_graph, n, INF)


    for answer in answers[1:]:
        print(' '.join(map(str, answer[1:])))
        

if __name__ == "__main__":
    main()
