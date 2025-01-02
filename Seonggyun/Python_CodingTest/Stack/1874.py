import sys

num_len = int(input())
num_list = []

for _ in range(num_len):
    num_list.append(int(sys.stdin.readline().strip()))
    
current_num = 1
stack = []
answers = []

for num in num_list:
    
    while current_num <= num:
        stack.append(current_num)
        answers.append("+")
        current_num += 1
    
    if stack[-1] == num:
        stack.pop()
        answers.append("-")
    
    else:
        print("NO")
        break

else:
    print('\n'.join(answers))