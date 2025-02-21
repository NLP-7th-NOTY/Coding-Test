import sys
from collections import defaultdict

def dfs(visited, parent_dict:dict, tree, parent_node):
    for node in tree[parent_node]: 
        if not visited[node]:
            visited[node] = True
            parent_dict[node] = parent_node
            # print(parent_dict)
            dfs(visited, parent_dict, tree, node)
            

def main():
    sys.setrecursionlimit(10**6)
    N = int(sys.stdin.readline().rstrip())
    tree = defaultdict(list)
    parent_dict = dict()
    visited = [False] * (N + 1)
    visited[1] = True
    
    for _ in range(N-1):
        node_1, node_2 = map(int, sys.stdin.readline().rstrip().split())
        tree[node_1].append(node_2)
        tree[node_2].append(node_1)
        
    dfs(visited, parent_dict, tree, 1)
    
    for node in range(2, N + 1):
        print(parent_dict[node])
        
        
if __name__ == "__main__":
    main()