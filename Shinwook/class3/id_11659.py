import sys

num_of_inputs, num_of_questions = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))


prefix_sum = [0] * (num_of_inputs + 1)
for i in range(num_of_inputs):
    prefix_sum[i + 1] = prefix_sum[i] + numbers[i]

for _ in range(num_of_questions):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start - 1])




