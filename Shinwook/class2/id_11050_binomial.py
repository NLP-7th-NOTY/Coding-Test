
num1, num2 = map(int, input().split())
result = 1
for i in range(num2):
    result *= (num1-i)
    result //= (i+1)


print(result)


