import sys
numbers = []
max = 0
for i in range(9):
    numbers.append(int(sys.stdin.readline()))
    if numbers[i] > numbers[max]:
        max = i

print(numbers[max])
print(max+1)
