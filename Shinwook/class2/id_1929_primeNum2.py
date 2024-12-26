import sys

min, max = list(map(int, sys.stdin.readline().split()))
prime_numbers=[]

divisor=0
result=0

for i in range(min, max+1):
    if i < 2:
        continue
    divisor = 0
    for j in range(i):
        if i % (j+1) == 0:
            if divisor == 3:
                break     
            else:
                divisor+=1
    if divisor == 2:
        prime_numbers.append(i)


for i in prime_numbers:
    print(i)



