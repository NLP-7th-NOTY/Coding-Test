import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    
    for _ in range(N):
        n = int(sys.stdin.readline().rstrip())
        
        # dp[i][0]: 무선택, dp[i][1]: 상단 선택, dp[i][2]: 하단 선택
        dp = [[0, 0, 0] for _ in range(n)]
        
        top = list(map(int, sys.stdin.readline().rstrip().split()))
        bottom = list(map(int, sys.stdin.readline().rstrip().split()))
        
        # 경우의 수는 총 세가지
        # 1. 열에서 아무것도 선택하지 않거나
        # 2. top(상단)에서 선택하거나
        # 3. bottom(하단)에서 선택하는 경우 총 세가지이다.
        # 다만 각 선택을 하는 경우에 이전 선택은 제약될 것이다. (ex. 상단에서 선택시 이전에 하단에서 선택했거나 아무것도 선택하지 않았어야 함.)
        # 위 포인트가 살짝 어려웠을 수도..!
        
        # 아무것도 선택하지 않은 경우 초기화        
        dp[0][0] = 0
        dp[0][1] = top[0]
        dp[0][2] = bottom[0]
        
        # 1부터 시작하는 이유는, 이전 선택을 고려하는 알고리즘인데 0부터 시작하면 -1은 없으므로 안 됨.
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) # 아무것도 선택하지 않는 경우에는 이전 선택지중 가장 큰 값이 오면 됨.
            dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + top[i]  # 상단을 선택하는 경우 이전 선택이 아무것도 선택하지 않았거나, 하단을 선택한 경우여야 함.
            dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + bottom[i]  # 하단을 선택하는 경우에 이전 선택이 아무것도 선택하지 않았거나, 상단을 선택했어야 함.

        # 세가지 경우가 고려된 case 중에서 max 추출
        print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))



if __name__ == "__main__":
    main()