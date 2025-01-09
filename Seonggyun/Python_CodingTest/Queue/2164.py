from collections import deque

N = int(input())

num_list = deque(range(1, N+1))

drop = num_list.popleft()

while num_list:
    move = num_list.popleft()
    num_list.append(move)
    drop = num_list.popleft()

print(drop)