import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    
    dp = []
    for _ in range(n):
        dp.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] += max(dp[i+1][j], dp[i+1][j+1])
    
    print(dp[0][0])
    

if __name__ == "__main__":
    main()
