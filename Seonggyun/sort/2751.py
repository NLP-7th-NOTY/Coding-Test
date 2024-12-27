# import sys

# num = int(input())

# num_list = [0]*1000001

# for _ in range(num):
#     temp = int(sys.stdin.readline().strip())
#     num_list[temp] = temp

# for number in range(1, 1000001):
#     if num_list[number] != 0:
#         print(num_list[number])
        
        
# import sys
# num = int(input())

# num_list = [0]*1000001

# for _ in range(1, num + 1):
#     temp = int(sys.stdin.readline().strip())
#     num_list[temp] += 1

# for number in range(1, 1000001):
#     if num_list[number] > 0:
#         print(number)

import sys
num = int(input())

num_list = []

for _ in range(num):
    num_list.append(int(sys.stdin.readline().strip()))
    
num_list.sort()

for _ in num_list:
    print(_)