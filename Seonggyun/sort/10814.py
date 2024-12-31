import sys
from collections import defaultdict

num = int(input())

age_dict = defaultdict(list)

for _ in range(num):
    age, name = sys.stdin.readline().strip().split()
    age_dict[int(age)].append(name)

age_list = list(age_dict.keys())
age_list.sort()

for key in age_list:
    length = len(age_dict[key])
    if length > 0:
        for name in age_dict[key]:
            print(key, name)
            
            
