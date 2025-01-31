# 알고리즘
def count_Ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # 아무 선택도 안하는 경우의 수
    
    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i - 1]
        
        if n >= 2:
            dp[i] += dp[i - 2]
            
        if n >= 3:
            dp[i] += dp[i - 3]
            
    return dp[n]
    
# 풀이 형식
def solve():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        print(count_Ways(n))
        
if __name__ == "__main__":
    solve()
    