# import sys
# from collections import defaultdict
# num_1 = int(input())

# num_dict = defaultdict(int)

# num_list_1 = list(map(int, sys.stdin.readline().strip().split()))

# for number_1 in num_list_1:
#     num_dict[number_1] += 1
    
# num_2 = int(input())

# answer = ''

# num_list_2 = list(map(int, sys.stdin.readline().strip().split()))

# for number_2 in num_list_2:
#     temp = num_dict[number_2]
#     answer += ' ' + str(temp)
    
# answer = answer.strip()

# print(answer)


# # int()의 경우 기본적으로 아무 인자도 전달받지 않으면 0을 반환한다.
# # print(int())의 경우 출력: 0
# # defaultdict에는 callable한 객체 또는 None을 넣어줄 것. 그냥 정수넣으면 안 됨.

"""
위 풀이는 시간복잡도 문제로 탈락
시간 복잡도가  **O(num_1 + 2*num_2)**에 해당...
그데 **빅 오 표기법**에서는 상수 계수 생략하므로 O(num_1 + num_2) 라고 생각하자...

"""
import sys
from collections import Counter

num_1 = int(input())
num_list_1 = list(sys.stdin.readline().strip().split())

num_2 = int(input())
num_list_2 = list(sys.stdin.readline().strip().split())

# Counter로 개수 새기
counter = Counter(num_list_1)

result = [str(counter[target_number]) for target_number in num_list_2]

answer = ' '.join(result)
print(answer)