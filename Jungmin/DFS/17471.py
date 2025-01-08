from itertools import combinations

N = int(input())
graph = [[-1, set()] for _ in range(N+1)]
arr = list(map(int, input().split()))
town = set(i for i in range(1, N+1))
tot = float('inf')
global n_town

def DFS(start, current, start_id, A, B, visited, res=False):
    global n_town

    if (start_id == 'A' and n_town == len(A)) or (start_id == 'B' and n_town == len(B)):
        return True

    for elem in graph[current][1]:
        if visited[elem] == -1 and ((start_id == 'A' and elem in A) or (start_id == 'B' and elem in B)):
            visited[elem] = 1
            n_town += 1
            res = DFS(start, elem, start_id, A, B, visited)
            visited[elem] = 0

        else:
            visited[elem] = 1

    return res

for i in range(N):
    graph[i+1][0] = arr[i]
    vertex = list(map(int, input().split()))

    for elem in vertex[1:]:
        graph[i+1][1].add(elem)
        graph[elem][1].add(i+1)

for i in range(1, N//2+1):
    possible = list(combinations(list(i for i in range(1, N+1)), i))
    global n_town

    for elem in possible:
        A = set(elem)
        B = town - A

        start = A.pop()
        A.add(start)
        visited = [-1 for _ in range(N+1)]
        visited[start] = 1
        n_town = 1
        res1 = DFS(start, start, 'A', A, B, visited)

        start = B.pop()
        B.add(start)
        visited = [-1 for _ in range(N+1)]
        visited[start] = 1
        n_town = 1
        res2 = DFS(start, start, 'B', A, B, visited)

        if res1 and res2:
            tot = min(tot, abs(sum(graph[i][0] for i in A)-sum(graph[i][0] for i in B)))

print(tot if tot != float('inf') else -1)