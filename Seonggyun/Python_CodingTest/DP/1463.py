import sys

N = int(sys.stdin.readline().rstrip())

def minimum_to_N(N):
    dp = [0]*(N + 1)
    
    # 2부터 시작, 1부터 시작하면 그 이후의 연산에도 영향을 미치게 됨.
    # 1부터 하게 되면 dp[2]가 2가 됨. 왜냐하면 dp[1]이 1이 되는데,
    # 그러면 dp[1]에 영향을 받아서 그럼
    for number in range(2, N+1):
        dp[number] = dp[number - 1] + 1 # 1로 빼서 이전꺼랑 더하면 되니까
        
        # 그런데 마냥 1만 빼서 이전꺼랑 더한다고 최적일 수 없음 배수일 수 있기 때문
        # 그래서 해당 배수 직전까지 배수까지 가서 거기서 +1 하는 방안을 고려
        # 그 사이에는 더 많은 연산을 요구하는 경우가 있는데 그걸 배수로 건너 뛰는 것
        if number % 3 == 0:
            dp[number] = min(dp[number], dp[number // 3] + 1)

        if number % 2 == 0:  
            dp[number] = min(dp[number], dp[number // 2] + 1)
        

    
    return dp[N]

print(minimum_to_N(N))