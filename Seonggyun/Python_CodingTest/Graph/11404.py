import sys

def floyd_warshall(n, cost_graph):

    # 플로이드–워셜 알고리즘 수행
    for k in range(1, n + 1):  # 경유지
        for i in range(1, n + 1):  # 출발 도시
            for j in range(1, n + 1):  # 도착 도시
                if cost_graph[i][j] > cost_graph[i][k] + cost_graph[k][j]:
                    cost_graph[i][j] = cost_graph[i][k] + cost_graph[k][j]

    # 도달할 수 없는 경우 0으로 변경
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if cost_graph[i][j] == float('inf'):
                cost_graph[i][j] = 0

    return cost_graph

def main():
    n = int(input())  # 도시 개수
    m = int(input())  # 버스 개수
    
    INF = float('inf')
    cost_graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자신에게서 자신으로 가는 것은 따로 예외처리해서 이렇게 0 -> 0 으로 만들어줘야 이후
    # 연산틀리지 않게 됨.
    for i in range(1, n + 1):
        cost_graph[i][i] = 0
    
    for _ in range(m):
        start, arrive, cost = map(int, sys.stdin.readline().rstrip().split())
        cost_graph[start][arrive] = min(cost_graph[start][arrive], cost)

    result = floyd_warshall(n, cost_graph)

    # 결과 출력
    for i in range(1, n + 1):
        print(" ".join(map(str, result[i][1:])))

if __name__ == "__main__":
    main()
