import sys
num = int(sys.stdin.readline())
result = 1
count = 0

for i in range(1, num + 1):
    result = (result * i)

for i in range(len(str(result))-1, -1, -1):
    if str(result)[i] == '0':
        count += 1
    else:
        break
print(count)