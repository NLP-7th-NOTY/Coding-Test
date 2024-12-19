while True:
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if num1 == 0 and num2 == 0:
        break
    else:
        print(num1+num2)