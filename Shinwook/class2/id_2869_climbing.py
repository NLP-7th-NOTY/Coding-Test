import sys

a, b, v = list(map(int, sys.stdin.readline().split()))
count=(v-a)//(a-b)+1
if (v-a)%(a-b) != 0:
    count +=1

print(count)

