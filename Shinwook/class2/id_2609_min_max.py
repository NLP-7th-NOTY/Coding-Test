num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

for i in range(num1):
    if num1%(i+1)==0 and num2%(i+1)==0:
        min = i+1
max= num1*num2/min
print(min)
print(int(max))