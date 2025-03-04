import sys

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    dp = [[0] * (N + 1) for _ in range(N)]
    
    # 루프를 통해 누적 합을 미리 구해주고
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = (num_list[i - 1][j - 1]  # 타겟 배열 끝단 값
                        + dp[i - 1][j]          # 타겟 배열 직전 행과 타겟배열 열의 누적합
                        + dp[i][j - 1]          # 타겟 배열 행과 타겟배열 직전 열의 누적합
                        - dp[i - 1][j - 1]      # 타겟배열 직전행, 직전 열의 누적합
                        )
    
    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
        answer = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
        print(answer)
    
    
if __name__ == "__main__":
    main()