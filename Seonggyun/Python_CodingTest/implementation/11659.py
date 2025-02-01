# 너무 느린 코드
# import sys

# N, M = map(int, sys.stdin.readline().rstrip().split())
# N_list = list(sys.stdin.readline().rstrip().split())


# for _ in range(M):
#     answer = 0

#     i, j = map(int, sys.stdin.readline().rstrip().split())
#     for index in range(i-1, j):
#         answer += int(N_list[index])
#     print(answer)

# 누적 합(Prefix Sum) 이용하여 시간복잡도는 O(1)로 처리하는 코드
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
N_list = list(map(int, sys.stdin.readline().rstrip().split()))

prefix_sum = [0] * (N + 1)

for index in range(1, N + 1):
    prefix_sum[index] = prefix_sum[index - 1] + N_list[index - 1]
    
for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[j] - prefix_sum[i-1])
    