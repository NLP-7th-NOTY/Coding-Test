import sys

num_of_pc = int(sys.stdin.readline())
num_of_pair = int(sys.stdin.readline())

visited = [False] * (num_of_pc + 1)
connect = [[] for _ in range(num_of_pc + 1)]
count = 0

for _ in range(num_of_pair):
    num1, num2 = map(int, sys.stdin.readline().split())
    connect[num1].append(num2)
    connect[num2].append(num1)
    
def dfs(start):
    global count
    visited[start] = True
    for next in connect[start]:
        if not visited[next]:
            count += 1
            dfs(next)
             
dfs(1)
print(count)






