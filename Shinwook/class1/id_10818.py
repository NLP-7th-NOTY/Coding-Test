import sys

number_of_inputs = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

min = numbers[0]
max = numbers[0]

for i in range(number_of_inputs):
    if numbers[i] < min:
        min = numbers[i]
    if numbers[i] > max:
        max = numbers[i]

print(min, max)
