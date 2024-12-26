import sys

count = int(sys.stdin.readline())
inputs= sys.stdin.readline()
numbers=[]

for i in range(count):
    numbers.append(int(inputs[i]))

print(sum(numbers))

