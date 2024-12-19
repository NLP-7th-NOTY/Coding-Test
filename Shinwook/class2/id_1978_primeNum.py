count = int(input())
divisor=0
result=0

while True:
    numbers=input().split()
    if len(numbers)==count:
        for i in range(count):
            numbers[i]=int(numbers[i])

            if numbers[i] < 0 or numbers[i] > 1000:
                print("숫자는 1000 이하인 자연수입니다.")
                continue

        break
    else:
        print("N과 입력한 숫자의 수가 맞지 않습니다.")

for i in range(count):
    divisor = 0
    for j in range(numbers[i]):
        if numbers[i] % (j+1) == 0:
            if divisor == 3:
                break     
            else:
                divisor+=1
    if divisor == 2:
        result += 1

print(result)



