import sys


def main():
    
    # 입력 받기
    N = int(sys.stdin.readline().rstrip())
    cost = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]
    
    # DP 테이블 초기화
    dp = [[0] * 3 for _ in range(N)]
    
    # 첫 번째 집 비용 초기화
    dp[0][0] = cost[0][0]
    dp[0][1] = cost[0][1]
    dp[0][2] = cost[0][2]
    
    # DP 점화식 계산
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
        
    
    print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
            
    
if __name__ == "__main__":
    main()
    
    
# 최적화(공간 최적화)
import sys

def main():
    # 입력 받기
    N = int(sys.stdin.readline().rstrip())
    cost = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]
    
    # 초기 비용
    prev = cost[0]

    # DP 점화식 계산
    for i in range(1, N):
        r = min(prev[i-1][1], prev[i-1][2]) + cost[i][0]
        g = min(prev[i-1][0], prev[i-1][2]) + cost[i][0]
        b = min(prev[i-1][0], prev[i-1][1]) + cost[i][0]
        prev = [r, g, b]
        
    print(min(prev))
    
    
if __name__ == "__main__":
    main()