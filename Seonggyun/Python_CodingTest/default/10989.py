import sys

N = int(input())
count = [0]*10001

for i in range(1, N+1):
    temp = int(sys.stdin.readline().strip())
    count[temp] += 1
    
for num in range(10001):
    if count[num] > 0:
        for _ in range(count[num]):
            print(num)
