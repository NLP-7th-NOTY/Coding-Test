# import sys


# def main():
    
#     n = int(sys.stdin.readline().rstrip())
    
#     # 백트래킹 함수: row번째 행에 퀸을 배치하는 함수
#     def backtrack(row):
#         # 기저 조건: 모든 행에 퀸을 배치했다면 (row == n) 경우의 수 1 추가
#         if row == n:
#             nonlocal count
#             count += 1
#             return  # 해당 backtrack 함수 끝내기
        
#         # 현재 행(row)에서 0부터 n - 1 까지 각 열(col)을 탐색함.
#         for col in range(n):
#             # 이미 해당 열(col)이나 두 대각선에 퀸이 존재한다면 건너뛰기
#             # row - col 하면 해당 지점 기준 좌측 대각선에 있는 row, col 조합의 값과 전부 일치
#             # row + col 하면 해당 지점 기준 우측 대각선에 있는 row, col 조합의 값과 전부 일치
#             if col in cols or (row - col) in diag1 or (row + col) in diag2:
#                 continue  # 이 위치는 퀸을 둘 수 없으므로 다음 열로(다음 for문으로) 이동
            
#             # 현재 위치에 퀸을 배치한다.
#             cols.add(col)       # 현재 열 사용 중
#             diag1.add(row - col)  # ↖↘ 대각선 사용중
#             diag2.add(row + col)  # ↙↗ 대각선 사용중
            
#             # 다음 행으로 넘어가 퀸 배치를 시도
#             backtrack(row + 1)
            
#             # backtracking: 이번 배치가 끝났으므로, 현재 행의 퀸을 제거하고 원상복구!
#             # 맨 처음 row == n 된 순간에 return 되며 해당 함수가 마쳐지고 순차적으로 이하 
#             # 회수가 시작되며 최종적으로 cols, diag1, diag2 모두 빈 set값으로 초기화 됨
#             # 그렇게 최초의 for문으로 돌아가 첫번째 행에서 열(col)이 다음 열로 넘어가고 거기에 퀸이 최초에 배치됨.
#             # 이런식으로 완전 탐색을 실시하는 것.
#             # 다만, 중간에 if 문을 통하여 일종의 가지치기를 통해 최적화 하는 것
#             cols.remove(col)  # row가 아니라 col을 제거해야함.
#             diag1.remove(row - col)
#             diag2.remove(row + col)
        
#     count = 0  # 가능한 배치 방법의 총 개수를 저장할 변수 backtrack 함수 내에서는 nonlocal을 통해 불러옴
    
#     # set을 사용하여 어떤 열과 어떤 대각선에 이미 퀸이 있는지 관리함. (행은 row 단위로 for문 통해 넘어가며 계산하므로 제외)
#     cols, diag1, diag2 = set(), set(), set()
#     backtrack(0)  # 0번째 행부터 탐색 시작
    
#     return print(count)


# if __name__ == "__main__":
#     main()
    
###############################

# 최적화 코드
import sys

def main():
    n = int(sys.stdin.readline().strip())

    def backtrack(row):
        nonlocal count
        if row == n:  # 모든 행에 퀸을 배치 완료한 경우
            count += 1
            return

        for col in range(n):  # 현재 행(row)의 각 열(col) 검사
            if colUsed[col] or diag1Used[row - col + n - 1] or diag2Used[row + col]:  # 이미 사용된 위치라면 패스
                continue
            
            # 퀸 배치
            colUsed[col] = diag1Used[row - col + n - 1] = diag2Used[row + col] = True
            backtrack(row + 1)
            
            # 백트래킹 (퀸 제거)
            colUsed[col] = diag1Used[row - col + n - 1] = diag2Used[row + col] = False

    count = 0
    colUsed = [False] * n
    
    # 대각선에 대한 정보를 인덱스로 접근해서 불리언으로 비교해주는 것이 매우 빠름.
    # 그런데 인전 처럼 단순히 row-col을 해버리면 음수 인덱스가 생성되어 버리니까
    # 그걸 막기 위해서 그냥 -(n-1) ~ 0 ~ (n+1) 이라는 수의 범위를 커버하기 위해 (2*n - 1)해 주고
    # row - col 에 음수 방지를 위해서 + (n - 1)을 해서 보정해주는 것
    # 우상향 대각선의 경우 (row + col)에는 음수 없이 자동으로 0 ~ (2n - 2) 범위를 지니므로 보정 불필요
    diag1Used = [False] * (2 * n - 1)  # 대각선 개수는 `2 * n - 1`
    diag2Used = [False] * (2 * n - 1)

    backtrack(0)
    print(count)

if __name__ == "__main__":
    main()
