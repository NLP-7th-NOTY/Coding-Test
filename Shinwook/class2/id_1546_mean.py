count = input()
count = int(count)
max=0


while True:
    numbers=input().split()
    if len(numbers)==count:
        for i in range(count):
            numbers[i]=int(numbers[i])

            if numbers[i] < 0 or numbers[i] > 100:
                print("성적은 100보다 작거나 같은 음이 아닌 정수입니다.")
            if numbers[i] > max:
                max = numbers[i]
        break
    else:
        print("과목의 개수와 성적의 수가 맞지 않습니다.")

print(sum(numbers)/max*100/count)

