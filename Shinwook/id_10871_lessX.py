count, comp = input().split()
count = int(count)
comp = int(comp)

while True:
    numbers=input().split()
    if len(numbers)==count:
        break

for i in range(count):
    if int(numbers[i])<comp:
        print(int(numbers[i]), end=" ")

