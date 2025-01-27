import sys

M = int(input())

S = set()
FULL_SET = set(map(str, range(1, 21)))

for _ in range(M):
    command = sys.stdin.readline().rstrip()
    com = command[:2]
    
    
    if com == "ad":
        _, mand = command.split()
        if mand in S:
            pass
        else:
            S.add(mand)
    
    
    elif com == "re":
        _, mand = command.split()
        if mand in S:
            S.remove(mand)
        else:
            pass
    
    
    elif com == "ch":
        _, mand = command.split()
        
        if mand in S:
            print(1)
        else:
            print(0)
    
    
    elif com == "to":
        _, mand = command.split()
        
        if mand in S:
            S.remove(mand)
        
        else:
            S.add(mand)
    
    
    elif com == "al":
        S = FULL_SET.copy()
        
    
    elif com == "em":
        S.clear()