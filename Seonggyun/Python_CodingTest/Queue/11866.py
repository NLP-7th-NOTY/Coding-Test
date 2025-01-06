import sys

N, K = map(int, sys.stdin.readline().strip().split())
N_list = [n for n in range(1, N+1)]
target_K = 0
answer_start = "<"
answer_middle = []
answer_end = ">"
answer = ""

while N_list:
    answer = N_list.pop(0)
    target_K += 1
    if target_K == K:
        answer_middle.append(str(answer))
        target_K = 0
    else:
        N_list.append(answer)

answer = ', '.join(answer_middle)

print(answer_start+answer+answer_end)