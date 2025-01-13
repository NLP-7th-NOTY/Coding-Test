import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
arr = deque(map(int, input().split()))
robot = deque(-1 for _ in range(2*N))
up, down, tot = 0, N-1, 0

while True:
    arr.rotate(1)
    robot.rotate(1)

    if robot[down] == 1:
        robot[down] = -1

    candidate = []
    for i in range(N-2, 0, -1):
        if robot[i] == 1:
            next = (i+1)%(2*N)
            if robot[next] == -1 and arr[next] >= 1:
                robot[i] = -1
                robot[next] = 1
                arr[next] -= 1

    if robot[down] == 1:
        robot[down] = -1

    if arr[up] != 0:
        robot[up] = 1
        arr[up] -= 1

    if sum(0 == arr[i] for i in range(2*N)) >= K:
        print(tot+1)
        exit()

    else:
        tot += 1
