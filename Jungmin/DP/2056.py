from collections import deque

N = int(input())
arr = [[-1, -1]]
arr.extend(list(map(int, input().split())) for _ in range(N))

to_go = [elem[1] for elem in arr]
relate = [[] for _ in range(N+1)]
end_time = [-float('inf') for _ in range(N+1)]
queue = deque([])
res = -1

for i, elem in enumerate(arr):
    if len(elem) > 2:
        for e in elem[2:]:
            relate[e].append(i)

    if elem[1] == 0:
        end_time[i] = 0

for i, elem in enumerate(to_go):
    if elem == 0:
        queue.append(i)

while sum(to_go) != -1:
    next_queue = deque([])
    while queue:
        pid = queue.popleft()
        for elem in relate[pid]:
            to_go[elem] -= 1
            end_time[elem] = max(end_time[elem], end_time[pid] + arr[pid][0])
            res = max(res, end_time[elem]+arr[elem][0])

            if to_go[elem] == 0:
                next_queue.append(elem)

        res = max(res, end_time[pid]+arr[pid][0])

    queue = next_queue
    del next_queue

print(max(e[0] for e in arr) if res == -1 else res)