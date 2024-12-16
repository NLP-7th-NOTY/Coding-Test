import heapq, sys
input = sys.stdin.readline

T = int(input())
res = []

for i in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    cache = {}
    k_list = [input().split() for _ in range(k)]

    for cmd in k_list:
        if cmd[0] == 'I':
            heapq.heappush(max_heap, -int(cmd[1]))
            heapq.heappush(min_heap, int(cmd[1]))

            if int(cmd[1]) in cache:
                cache[int(cmd[1])] += 1

            else:
                cache[int(cmd[1])] = 1

        elif cmd[0] == 'D':
            if cmd[1] == '1':
                while max_heap and cache[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    cache[max_val] -= 1

            if cmd[1] == '-1':
                while min_heap and cache[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    cache[min_val] -= 1

    while min_heap and cache[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    while max_heap and cache[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if max_heap:
        res.append(f"{-1 * max_heap[0]} {min_heap[0]}")

    else:
        res.append("EMPTY")

for elem in res:
    print(elem)