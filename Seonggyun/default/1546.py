import sys

number = int(input())

num_list = list(map(int, sys.stdin.readline().strip().split()))


num_max = max(num_list)
num_min = min(num_list)

answer = []

for num in num_list:
    new_num = (num/num_max)*100
    answer.append(new_num)
    
print(sum(answer)/len(answer))