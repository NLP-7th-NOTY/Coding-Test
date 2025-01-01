import sys

order_num = int(input())

stack = []

for _ in range(order_num):
    order_list = list(sys.stdin.readline().strip().split())
    if order_list[0] == 'push':
        stack.append(int(order_list[1]))
    else:
        if order_list[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                result = stack.pop()
                print(result)
            
        elif order_list[0] == 'size':
            result = len(stack)
            print(result)
        
        elif order_list[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        
        elif order_list[0] == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
            
