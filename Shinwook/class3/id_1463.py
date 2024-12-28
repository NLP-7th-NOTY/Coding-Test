import sys

num = int(sys.stdin.readline())
num_list = [0] * (num+1)

for i in range(2, num+1):
    num_list[i] = num_list[i-1] + 1
    if i % 3 == 0:
        num_list[i] = min(num_list[i], num_list[i//3] + 1)
    if i % 2 == 0:
        num_list[i] = min(num_list[i], num_list[i//2] + 1)

print(num_list[num])

