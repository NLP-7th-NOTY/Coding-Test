import sys
from collections import defaultdict

num = int(input())
num_pair = int(input())

network_dict = defaultdict(list)
answer = []



for _ in range(num_pair):
    computer_1, computer_2 = map(int, sys.stdin.readline().rstrip().split())
    network_dict[computer_1].append(computer_2)  # 단반향으로만 추가하는 경우에는 2 1 이렇게 들어오는 경우 경로 못찾음
    network_dict[computer_2].append(computer_1)  # 양방향 등록
        
visited = set()

def dfs(start):
    visited.add(start)
    connection = network_dict[start]
    
    for connect in connection:
        if connect not in visited:
            answer.append(connect)
            dfs(connect)
    
dfs(1)

answer = set(answer)
answer.discard(1)
print(len(answer))