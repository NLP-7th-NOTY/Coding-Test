number = int(input())

for num in range(1, number+1):
    result = ' '*(number - num) + '*'*num
    print(result)