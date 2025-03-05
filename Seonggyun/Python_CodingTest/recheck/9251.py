import sys


def main():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    len_1 = len(s1)
    len_2 = len(s2)
    
    # DP 테이블 생성
    dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)] 
    
    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            
            # 만약 문자가 같다면 두 문자열의 이전 부분에서의 LCS 길이에 
            # 현재 일치하는 문자를 추가하여 + 1을 해준다.
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            
            # 그렇지 않다면, 즉 두 문자가 다른 경우에는
            # dp[i-1][j], s1의 i번째 문자를 제외한 경우의 LCS 길이 또는
            # dp[i][j-1], s2의 j번째 문자를 제외한 경우의 LCS 길이
            # 두 문자 중 어느 하나는 LCS에 포함될 수 없는 상태이므로
            # 위 둘 중 최대값을 찾아 dp[i][j]에 넣어준다.
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    print(dp[len_1][len_2])


if __name__ == "__main__":
    main()