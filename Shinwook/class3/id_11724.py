import sys

num_of_node, num_of_edge = map(int, sys.stdin.readline().split())

connect = [[] for _ in range(num_of_node + 1)]

for _ in range(num_of_edge):
    num1, num2 = map(int, sys.stdin.readline().split())
    connect[num1].append(num2)
    connect[num2].append(num1)
    


