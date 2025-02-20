import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A_list = list(map(int, sys.stdin.readline().rstrip().split()))
    
    # dp 초기화
    # dp[0], 즉 A_list[0]을 마지막 원소로 갖는 경우 1이어야 하므로...
    # 그리고 다른 모든 원소들도 각각이 마지막 원소일 때에 최장 부분 수열의
    # 길이의 최솟값은 1이므로 요소를 1로 초기화하고 길이는 N만큼
    dp = [1] * N
    
    # 이제 자기의 자리수보다 이전 자리수와의 전부 비교를 통해서
    # 이전 자리수까지의 최대 길이 + 1 을 자기 자신의 위치에서부터
    # 이전 모든 요소의 위치까지 비교를 통해 갱신함
    for i in range(N):
        for j in range(i):
            if A_list[j] < A_list[i]:
                # 아래 +1 은 이전 자리수에서 
                # 지금 i번째 원소가 마지막으로 온 경우라서 
                # +1 만큼 길이가 늘어난 것'
                # 마지막으로 못 올 수도 있지 않냐고?
                # 아니 ㅋㅋ 그래서 위에서 조건문을통해 큰 경우가
                # 검증 되어야 올 수 있게끔 한 것.
                dp[i] = max(dp[i], dp[j] + 1) 

    print(max(dp))
    return

if __name__ == "__main__":
    main()