import sys

while True:
    inputs =sys.stdin.readline().strip()
    if inputs=="0":
        break
    result = "yes"

    for i in range(len(inputs)//2):
        if inputs[i] != inputs[len(inputs)-(i+1)]:
            result = "no"
            break
        
    print(result)