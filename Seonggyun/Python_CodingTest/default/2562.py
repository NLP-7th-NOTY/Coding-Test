import sys
nums = []

for _ in range(9):
    temp = int(sys.stdin.readline().strip())
    nums.append(temp)

    
max_num = max(nums)
num_index = nums.index(max_num)

print(max_num)
print(num_index + 1)