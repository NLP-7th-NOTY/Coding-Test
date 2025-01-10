import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0 for _ in range(10*N)]
res = []

def make_tree(idx, start, end):
    if start == end:
        tree[idx] = [arr[start], arr[start]]
        return tree[idx]

    mid = (start+end)//2
    left = make_tree(idx*2, start, mid)
    right = make_tree(idx*2+1, mid+1, end)

    tree[idx] = [min(left[0], right[0]), max(left[1], right[1])]
    return tree[idx]

def query(node_left, node_right, idx_left, idx_right, idx):
    if idx_right < node_left or idx_left > node_right:
        return [float('inf'), -float('inf')]

    if idx_left <= node_left <= node_right <= idx_right:
        return tree[idx]

    mid = (node_left+node_right)//2
    left = query(node_left, mid, idx_left, idx_right, idx*2)
    right = query(mid+1, node_right, idx_left, idx_right, idx*2+1)

    return [min(left[0], right[0]), max(left[1], right[1])]

make_tree(1, 0, N-1)
for i in range(M):
    idx_left, idx_right = map(int, input().split())
    res.append(query(0, N-1, idx_left-1, idx_right-1, 1))

for elem in res:
    print(str(elem)[1:-1].replace(",",""))