import sys

def cut_off(left, right, trees):
    bring = 0
    mid = (left + right) // 2
    
    for tree in trees:
        cut = tree - mid
        if tree > mid:
            bring += cut
    
    return bring, mid
        
        
def best_cut_off(left, right, trees):
    best_height = 0
    while left <= right:
        bring, mid = cut_off(left, right, trees)
        
        if bring >= M:
            best_height = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return best_height


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    trees = list(map(int, sys.stdin.readline().rstrip().split()))

    right = max(trees)
    left = 0
    print(best_cut_off(left, right, trees))