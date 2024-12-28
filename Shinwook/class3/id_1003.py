import sys

count = int(sys.stdin.readline())

for _ in range(count):
    num = int(sys.stdin.readline())
    num_list = [[0, 0] for _ in range(num+1)]
    for i in range(num+1):
        if i == 0:
            num_list[i] = [1, 0]
        elif i == 1:
            num_list[i] = [0, 1]
        else:
            num_list[i] = [num_list[i-1][0] + num_list[i-2][0], num_list[i-1][1] + num_list[i-2][1]]
    print(num_list[num][0], num_list[num][1])






