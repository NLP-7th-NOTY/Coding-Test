import sys

count = int(sys.stdin.readline())
age_name = []

for _ in range(count):
    age, name = sys.stdin.readline().split()
    age_name.append((int(age), name))

age_name.sort(key=lambda x: x[0])

for age, name in age_name:
    print(age, name)