from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split()))[1:] for _ in range(M)]
graph = [[-1, []] for _ in range(N+1)]
queue = deque([])
check_idx = -1

def TOP(queue):
    visited = [0 for _ in range(N+1)]
    res = []
    while queue:
        current = queue.popleft()
        visited[current] = 1
        res.append(current)

        for elem in graph[current][1]:
            graph[elem][0] -= 1

            if graph[elem][0] == 0:
                queue.append(elem)

    if sum(visited) != N:
        return [0]

    else:
        return res

for elem in arr:
    for i, edge in enumerate(elem):
        if graph[edge][0] == -1:
            graph[edge][0] = 0
            check_idx = edge

        if i != 0:
            start, end = elem[i-1], edge
            graph[end][0] += 1
            graph[start][1].append(end)

for i in range(1, N+1):
    if graph[i][0] == -1:
        graph[i][0] = 0
        graph[check_idx][0] += 1
        graph[i][1].append(check_idx)

for i in range(len(graph)):
    if graph[i][0] == 0:
        queue.append(i)

res = TOP(queue)

for elem in res:
    print(elem, end='\n')