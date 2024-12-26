import heapq, sys
input = sys.stdin.readline
N, M, X = map(int, input().split())
metrix = [[] for _ in range(N+1)]
rev_metrix = [[] for _ in range(N+1)]

res = [0]
for i in range(M):
    s, e, l = map(int, input().split())
    metrix[s].append([e,l])
    rev_metrix[e].append([s, l])

def dij(start, metrix):
    queue = [[start, 0]]
    length = [float('inf') for _ in range(N+1)]
    length[start] = 0

    while queue:
        s, l = heapq.heappop(queue)

        if length[s] < l:
            continue

        for elem in metrix[s]:
            e, l = elem
            if length[s] + l < length[e]:
                length[e] = length[s] + l
                heapq.heappush(queue, [e, length[e]])

    return length

res = [x+y for x,y in zip(dij(X, rev_metrix), dij(X, metrix))]
print(sorted(res)[-2])