# import sys
# import heapq

# def main():
#     N = int(sys.stdin.readline().rstrip())
#     n_list = list(map(int, sys.stdin.readline().rstrip().split()))
#     n_set = set(n_list)
    
#     n_list_sorted = []
#     n_dict = dict()
    
#     for n in n_set:
#         heapq.heappush(n_list_sorted, n)
        
#     for i in range(0, len(n_set)):
#         x = heapq.heappop(n_list_sorted)
#         n_dict[x] = f"{i}"
    
#     target = []
    
#     for n in n_list:
#         target.append(n_dict[n])
    
#     answer = " ".join(target)
    
#     print(answer)

# if __name__ == "__main__":
#     main()
        
"""
위에 코드도 맞는 풀이지만, 시간복잡도와 메모리 사용량이 높음.

위에 첫 번째 코드: 159,312 KB
아래 두 번째 코드: 184,644 KB

- 약 25MB 차이가 발생하는 이유:
두 번째 코드는 추가적인 리스트(n_list_sorted)를 생성
heapq 자체의 메모리 오버헤드 존재


첫 번째 코드: 1,320ms
두 번째 코드: 2,040ms
- 실행 시간의 차이는 위와 같은데 약 720ms 차이가 발생하는 이유는

heapq의 push/pop 연산이 각각 필요하고
추가적인 리스트 순회가 필요하기 때문.
따라서 아래처럼 바꾼 코드가 더 좋음.
"""

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    
    # 복잡도 = O(n logn)
    sorted_unique_n_list = sorted(set(n_list))
    
    # 숫자에 대하여 순위 매기는 사전 생성
    n_dict = {n: str(i) for i, n in enumerate(sorted_unique_n_list)}
    
    # 원본 리스트에 대해 순위를 매기고 출력함. 딕셔너리 거치게 하면 됨.
    
    answer = " ".join(n_dict[n] for n in n_list)
    
    print(answer)

if __name__ == "__main__":
    main()
