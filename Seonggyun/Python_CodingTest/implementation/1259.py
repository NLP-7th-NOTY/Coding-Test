import sys

while True:
    string = list(sys.stdin.readline().rstrip())
    
    if string[0] == '0':
        break
    
    length = len(string)
    
    if length % 2 == 0:
        while length:
            first = string.pop(0)
            last = string.pop()
            length = len(string)
            
            if first != last:
                print('no')
                break
        
        else:
            print('yes')
    
    else:
        while length >= 3:
            first = string.pop(0)
            last = string.pop()
            length = len(string)
            
            if first != last:
                print('no')
                break
        
        else:
            print('yes')
                
                
            
