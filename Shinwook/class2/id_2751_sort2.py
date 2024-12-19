import sys

count = int(sys.stdin.readline())
numbers=[]

for _ in range(count):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for num in numbers:
    print(num)

'''

count = int(sys.stdin.readline())
numbers=[]

for i in range(count):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()

for j in range(count):
    print(numbers[j])


'''
