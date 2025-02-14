import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    
    # 회의시간 초기화
    meetings = []
    
    # 회의 시간 리스트로 받기
    for _ in range(N):
        meeting = tuple(map(int, sys.stdin.readline().rstrip().split()))
        meetings.append(meeting)
    
    # 끝나는 시간 기준 정렬하고 끝나는시간 같으면 시작 시간 기준 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))
    
    
    # 그리디 알고리즘 적용
    count = 0
    end_time = 0
    
    for start, end in meetings:
        if start >= end_time:
            count += 1
            end_time = end
    
    print(count)
    



















if __name__ == "__main__":
    main()
    
    