import sys

while True:
    numbers = list(map(int, sys.stdin.readline().split()))
    count=0
    max = 0 
       
    for i in range(3):
        numbers[i] = int(numbers[i])
        if numbers[i] == 0:
            count+=1
        if numbers[max] < numbers[i]:
            max = i
    if count ==3:
        break

    if numbers[max]**2 == numbers[max-1]**2 + numbers[max-2]**2:
        print("right")
    else:
        print("wrong")