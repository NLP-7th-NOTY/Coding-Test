import sys
from copy import deepcopy

N, M = map(int, sys.stdin.readline().rstrip().split())
card_list = list(map(int, sys.stdin.readline().rstrip().split()))
card_len = len(card_list)
m = 0
before_r = deepcopy(M)
answer = 0

# 전체 조합 만들기
# 맨 앞에서 한장 고르고 뒤에 하나도 안 고르다가 마지막에 두개 고를 수 있으므로 2장 남겨놓는다.
for n_1 in range(card_len - 2):  
    # 맨 앞에서 한 장 골랐으면 바로 그 뒤부터 시작해야하고, 마지막 한장은 맨 뒤에 올수 있으므로 1장 남겨 놓음
    for n_2 in range(n_1 + 1, card_len - 1):
        # 그 앞에서 한장 골랐으면 바로 그 뒤부터 시작해야하고, 이제 마지막 한장에 대한 자유도는 나에게 있으므로 따로 빼지 않음
        for n_3 in range(n_2 + 1, card_len):
            m = card_list[n_1] + card_list[n_2] + card_list[n_3]
            r = M - m 
            if r >= 0 and r < before_r:
                answer = m
                before_r = r

print(answer)
            
            
        