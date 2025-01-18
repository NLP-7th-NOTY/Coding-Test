from collections import deque

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def move(arr, R):
    y_start, y_end = 0, N
    x_start, x_end = 0, M
    while y_start < y_end and x_start < x_end:
        queue = deque([])

        for i in range(y_start, y_end):
            queue.append(arr[i][x_start])

        queue.pop()
        for i in range(x_start, x_end):
            queue.append(arr[y_end-1][i])

        queue.pop()
        for i in range(y_end-1, y_start-1, -1):
            queue.append(arr[i][x_end-1])

        queue.pop()
        for i in range(x_end-1, x_start-1, -1):
            queue.append(arr[y_start][i])

        queue.pop()
        amount = R % len(queue)

        for i in range(amount):
            queue.appendleft(queue.pop())

        for i in range(y_start, y_end):
            arr[i][x_start] = queue.popleft()

        queue.appendleft(-1)
        for i in range(x_start, x_end):
            elem = queue.popleft()
            if elem != -1:
                arr[y_end-1][i] = elem

        queue.appendleft(-1)
        for i in range(y_end-1, y_start-1, -1):
            elem = queue.popleft()
            if elem != -1:
                arr[i][x_end-1] = elem

        queue.appendleft(-1)
        for i in range(x_end-1, x_start, -1):
            elem = queue.popleft()
            if elem != -1:
                arr[y_start][i] = elem

        y_start, x_start, y_end, x_end = y_start + 1, x_start + 1, y_end - 1, x_end - 1

    return arr

arr = move(arr, R)
for elem in arr:
    print(str(elem)[1:-1].replace(',', ''))
