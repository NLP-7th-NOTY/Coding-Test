import sys

numbers=set()

for _ in range(10):
    num_of_input = int(sys.stdin.readline())
    numbers.add(num_of_input % 42)

print(len(numbers))
