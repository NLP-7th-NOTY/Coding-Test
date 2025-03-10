import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    tree = defaultdict(list)
    
    for _ in range(n - 1):
        parent, child, weight = map(int, input().rstrip().split())
        tree[parent].append((child, weight))
        tree[child].append((parent, weight))
    
    def dfs(node, dist):
        nonlocal max_distance, farthest_node  # 🔥 중요: 바깥 변수 사용
        if dist > max_distance:
            max_distance = dist
            farthest_node = node
        
        for next_node, weight in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dfs(next_node, dist + weight)

    # Step 1: 루트(1)에서 가장 먼 노드 찾기
    visited = [False] * (n + 1)
    max_distance = 0
    farthest_node = 0    

    visited[1] = True
    dfs(1, 0)
    
    # Step 2: farthest_node에서 가장 먼 노드 찾기
    visited = [False] * (n + 1)
    max_distance = 0

    visited[farthest_node] = True
    dfs(farthest_node, 0)
    
    print(max_distance)

if __name__ == "__main__":
    main()