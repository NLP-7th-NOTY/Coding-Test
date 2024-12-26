num = input()
num = int(num)
for i in range(num):
    print(" " * (num - i - 1) + "*" * (i + 1))


