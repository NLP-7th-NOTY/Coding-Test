import sys


def main():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    dp = [0] * (K + 1) # 무게가 0 ~ K일때 최대치 만족도 넣어놓는 dp
    
    for _ in range(N):
        w, v = map(int, sys.stdin.readline().rstrip().split())
        
        # K라는 최대 무게 설정치부터 w까지 하나씩 내려가며 갱신
        for current_weight in range(K, w - 1, -1):
            dp[current_weight] = max(dp[current_weight], dp[current_weight - w] + v)
        
    print(dp[K])

if __name__ == "__main__":
    main()