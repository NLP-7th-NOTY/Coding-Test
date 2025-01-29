"""
# 재귀 방식은 너무 오래 걸림.

def fibonaci(n):
    global answer_1
    global answer_0
    if n > 1:
        return fibonaci(n-1) + fibonaci(n-2)
    else:
        if n == 1:
            answer_1 += 1
            return 1
        else:
            answer_0 += 1
            return 0
        
T = int(input())

for _ in range(T):
    answer_0 = 0
    answer_1 = 0
    N = int(input())
    fibonaci(N)
    print(answer_0, answer_1)

"""


def fibonaci(n):
    
    dp = [[0, 0] for _ in range(n + 2)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
        
    return dp[n][0], dp[n][1]

T = int(input())

for _ in range(T):
    n = int(input())
    print(*fibonaci(n))    