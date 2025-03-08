import sys
import heapq

def dijkstra(start, graph, V):
    INF = float('inf')
    
    # 모든 정점까지의 거리를 무한대로 초기화 (시작점 제외), 왜 무한대? => 못 가게 되면 무한대로 출력하기로 문제에서 정함
    dist = [INF] * (V + 1)
    
    # 시작점의 경우 0으로 초기화
    dist[start] = 0
    
    # (거리, 정점)을 저장할 우선순위 큐(최소 힙)
    pq = []
    
    # heapq.push(pq, (거리, 정점번호)) : 튜플의 첫번째 원소를 기준으로 정렬됨.
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_dist, u = heapq.heappop(pq)  # 제일 짧은 거리에 있는 녀석이 튀어나옴
        if current_dist > dist[u]:
            continue  # 이미 더 짧은 경로가발견 되었으므로 무시한다.
        
        # 정점 u에서 뻗어나가는 모든 정점 v로의 거리 갱신 시도 (간선이 여러개 있을 수 있음)
        for v, weight in graph[u]:
            if dist[v] > current_dist + weight:  # 만약 현재 거리 사전이 더 길다? 그럼
                dist[v] = current_dist + weight  # 아래처럼 갱신
                heapq.heappush(pq, (dist[v], v))
    
    return dist     
    

def main():
    V, E = map(int, sys.stdin.readline().rstrip().split())
    K  = int(sys.stdin.readline().rstrip())
    
    # 그래프 초기화 (단방향 그래프)
    graph = [[] for _ in range(V + 1)]
    
    # E: 간선의 갯수 만큼 graph 초기화 값 설정
    for _ in range(E):
        # u에서 v로 가는 가중치 w만큼의 간선
        u, v, w = map(int, sys.stdin.readline().rstrip().split())
        
        graph[u].append((v, w))
        
    distances = dijkstra(K, graph, V)
    
    for i in range(1, V + 1):
        if distances[i] == float('inf'):
            print("INF")
        else:
            print(distances[i])


if __name__ == "__main__":
    main()