import sys

while True:
    temp = list(map(int, sys.stdin.readline().strip().split()))
    temp.sort()
    large = temp.pop()
    if large ==0:
        break
    
    else:
        if large*large == temp[0]**2 + temp[1]**2:
            print('right')
        else:
            print('wrong')
        