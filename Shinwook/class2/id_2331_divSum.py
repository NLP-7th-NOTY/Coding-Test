#N의 분해합 = N + 각 자리수의 합
#어떤 자연수 M의 분해합 = N인 경우, M을 N의 생성자라고 한다.
#자연수 N이 주어졌을 때, 가장 작은 생성자 M을 구하여라.

import sys

number = int(sys.stdin.readline())
m = 0

while True:
    m+=1
    if m + sum(map(int, str(m))) == number:
        print(m)
        break
    if m > number:
        print(0)
        break



