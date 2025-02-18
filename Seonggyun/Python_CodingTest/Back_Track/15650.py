import sys

def generate_combinations(n: int, m: int) -> None:
    """1부터 n까지 숫자중 m개 선택하여 조합 생성"""
    
    def backtrack(start: int, combination: list[int]) -> None:
        """현재 조합을 구성하고, 조건 만족시 출력하는 백트래킹 함수"""
        
        # 조합의 길이가 목표 m에 도달하면 출력
        if len(combination) == m:
            print(' '.join(map(str, combination)))
            return
        
        # start부터 n까지 숫자를 하나씩 선택
        for num in range(start, n + 1):
            combination.append(num) # 숫자를 추가하고
            backtrack(num + 1, combination) # 시작 숫자를 1 추가하여 오름차순으로 검증
            combination.pop() # 위에서 return 되었다면 해당 수열에서 마지막 pop 하고 for문 동작
        
    backtrack(1, []) # 조합 탐색 시작 -> 1부터 시작


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    generate_combinations(n, m)
    
    
    
# 다른 풀이
import sys
from itertools import combinations

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    
    results = None
    results = combinations(range(1, n + 1), m)
    
    for combination in results:
        print(' '.join(map(str, combination)))
    


if __name__ == "__main__":
    main()