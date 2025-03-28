import sys

def bellman_ford(n, edges):
    # 모든 정점의 거리를 0으로 초기화 
    # (음의 사이클 찾기 위해 모든 노드를 시작점으로 고려)
    dist = [0] * (n + 1)

    # n-1번 반복하여 최단 경로 찾기
    for _ in range(n - 1):
        for s, e, t in edges:
            if dist[s] + t < dist[e]:
                dist[e] = dist[s] + t

    # 음의 사이클 존재 여부 확인
    for s, e, t in edges:
        if dist[s] + t < dist[e]:
            return "YES"

    return "NO"

def main():
    # 테스트 케이스 수 입력
    tc = int(sys.stdin.readline())

    for _ in range(tc):
        # 지점 수, 도로 수, 웜홀 수 입력
        n, m, w = map(int, sys.stdin.readline().split())
        
        # 간선 정보 저장할 리스트
        edges = []

        # 도로 정보 입력 (양방향)
        for _ in range(m):
            s, e, t = map(int, sys.stdin.readline().split())
            edges.append((s, e, t))
            edges.append((e, s, t))

        # 웜홀 정보 입력 (단방향)
        for _ in range(w):
            s, e, t = map(int, sys.stdin.readline().split())
            edges.append((s, e, -t))

        # 벨만-포드 알고리즘으로 시간 여행 가능성 판단
        print(bellman_ford(n, edges))


if __name__ == "__main__":
    main()