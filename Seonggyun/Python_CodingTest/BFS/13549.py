import sys
from collections import deque

def bfs(N, K):
    # 위치의 최대 범위 (0부터 100000까지)    
    MAX = 100000
    
    # 방문 여부 및 해당 위치까지의 최소 시간을 저장하는 배열
    # -1 인 경우에는 방문하지 않은 것
    visited = [-1] * (MAX + 1)  # 방문 여부 및  최소 시간 저장
    
    # BFS 탐색을 위한 덱 초기화
    dq = deque([N])
    
    # 시작 위치에 대해서 방문 처리
    visited[N] = 0
    
    while dq:
        x = dq.popleft()  # 현재 위치를 꺼내고
        
        if x == K:
            return visited[x]  # 동생 찾았으면 종료함. x위치가 K와 일치하면 그대로 끝
        
        # 1. 순간이동 (가중치 0: 무슨의미? => 이동한다고 해서 소요시간이 발생하지 않음)
        # 조건은 범위 내에 존재하고 '미방문' 일 것
        if 2 * x <=  MAX and visited[2 * x] == -1:
            
            # 이전 위치의 시간 그대로 유지해준다.(시간을 그대로 옮겨와 줄 것. visited 안에 요소들은 방문 여부 + 시간이 함께 저장되어 있음)
            visited[2 * x] = visited[x]  
            
            # 이제 해당 위치가 dq로 옴
            dq.appendleft(2 * x)
            
        # 2. 걷는 경우 (가중치 1: 즉, 시간이 1초 증가함)
        for nx in (x -1, x + 1):  # 왼쪽, 오른쪽으로 이동하는 경우의 수
            if 0 <= nx <= MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1  # 현재 위치 시간 + 1
                dq.append(nx)  # 일반적인 BFS 방식으로 덱의 뒤에 추가


def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(N, K))
    

if __name__ == "__main__":
    main()