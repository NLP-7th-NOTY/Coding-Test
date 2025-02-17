import sys

# 아래 식에서 주의깊게 볼 건 각 사분면에 따라서 최종적으로 1,2,3을 더하게 된다는 것
def devide(N, r, c):
    if N == 0:
        return 0
    
    half = 2 ** (N - 1)
    
    # 좌상
    if r < half and c < half:
        # 해당 분기에서 좌상에 있으면 별도로 뭐 더할 필요 없음
        return devide(N - 1, r, c)
    
    # 우상
    if r < half and c >= half:
        return 1 * half**2 + devide(N - 1, r, c - half)
    
    # 좌하
    if r >= half and c < half:
        return 2 * half**2 + devide(N - 1, r - half, c)
    
    # 우하
    else:
        return 3 * half**2 + devide(N - 1, r - half, c - half)
    


def main():
    N, r, c = map(int, sys.stdin.readline().rstrip().split())
    print(devide(N, r, c))
    
    





if __name__ == "__main__":
    main()