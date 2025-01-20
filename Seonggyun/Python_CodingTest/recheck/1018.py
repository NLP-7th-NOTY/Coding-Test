import sys

def count_changes(board, start_row, start_col, color):
    changes = 0
    
    # 8x8 체스판 영역을 확인하면서 변경해야하는 칸 수를 셈
    for i in range(8):
        for j in range(8):
            expected_color = color if (i + j) % 2 == 0 else ('B' if color == 'W' else 'W')
            if board[start_row + i][start_col + j] != expected_color:
                changes += 1
                
    return changes

def min_painting_changes(board, n, m):
    min_changes = float('inf')
    
    # 가능한 모든 8x8 영역 탐색
    for i in range(n - 7):
        for j in range(m - 7):
            # 첫 번째의 경우에 왼쪽 위가 W
            changes_case1 = count_changes(board, i, j, 'W')
            
            # 두 번째의 경우에 왼쪽 위가 B
            changes_case2 = count_changes(board, i, j, 'B')
            
            # 두 경우 중 최소값을 구한다.
            min_changes = min(min_changes, changes_case1, changes_case2)
    
    return min_changes

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]

result = min_painting_changes(board, N, M)
print(result)