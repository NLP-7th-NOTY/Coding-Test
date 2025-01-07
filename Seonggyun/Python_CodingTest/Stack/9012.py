import sys

num = int(input())
answer = ""


for _ in range(num):
    ps_list = list(sys.stdin.readline().strip())
    
    if (ps_list[0] == ')') or (ps_list[-1] == '('):
        answer = "NO"
    
    else:
        stack = []
        for ps in ps_list:
            stack.append(ps)
            
            if (stack[0] == '(') and (stack[-1] == ')'):
                first = stack.pop(0)
                last = stack.pop()
        
        if stack:
            answer = "NO"
        
        else:
            answer = "YES"
    
    print(answer)
                
            
    