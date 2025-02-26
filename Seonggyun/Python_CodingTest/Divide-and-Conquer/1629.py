import sys

def power_mod(A:int, B:int, C:int):
    
    # B가 1인 경우에 재귀 멈추고 거꾸로 타고 올라가며 연산 시작
    if B == 1:
        return A % C
    
    # 모듈러 연산 적용
    # 최종적으로 어떻게든 B가 1이 되고, 그때 A % C 에서부터 타고 위로 올라가며 계산됨.
    # half에 해당 A % C가 담기면 실질적으로 A^2 % C = ((A % C) ^ 2) % C 가 적용되며
    # 모듈러 연산이 이하 식을 통해 이루어 짐.
    partial_result = power_mod(A, B//2, C)
    squared_result = (partial_result*partial_result) % C
    
    # 다만, B // 2 를 통하여 현재 '몫'에 해당하는 값만 쓰고 있는바(소숫점 이하 버림)
    # B가 홀수인 경우에 아래에서 타고 올라오면서 1만큼씩 비므로 아래 처럼 보완
    if B % 2 !=0:
        return (squared_result * A) % C
    
    else:
        return squared_result


def main():
    A, B, C = map(int, sys.stdin.readline().rstrip().split())
    
    print(power_mod(A, B, C))


if __name__ == "__main__":
    main()