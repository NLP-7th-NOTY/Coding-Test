import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(M+K)]
res = []
def init(tree_idx, left, right):
    if left == right:
        tree[tree_idx] = arr[left] % 1000000007
        return tree[tree_idx]

    mid = (left + right) // 2
    tree[tree_idx] = (init(tree_idx * 2, left, mid) * init(tree_idx * 2 + 1, mid+1, right)) % 1000000007

    return tree[tree_idx]

def update(tree_idx, update_idx, update_num, left, right):
    if right < update_idx or update_idx < left:
        return tree[tree_idx]

    if update_idx == left == right:
        tree[tree_idx] = update_num % 1000000007
        return tree[tree_idx]

    elif left == right:
        return tree[tree_idx]

    mid = (left + right) // 2
    tree[tree_idx] = (update(tree_idx * 2, update_idx, update_num, left, mid) * update(tree_idx * 2 + 1, update_idx, update_num, mid+1, right)) % 1000000007

    return tree[tree_idx]

def query(tree_idx, node_left, node_right, search_left, search_right):
    if node_right < search_left or search_right < node_left:
        return 1

    elif search_left <= node_left <= node_right <= search_right:
        return tree[tree_idx]

    mid = (node_left + node_right) // 2
    return (query(tree_idx * 2, node_left, mid, search_left, search_right) *
            query(tree_idx * 2 + 1, mid + 1, node_right, search_left, search_right)) % 1000000007


tree = [-1 for _ in range(4 * N)]
init(1, 0, N - 1)
for elem in cmd:
    c, b, a = elem
    if c == 1:
        update(1, b-1, a, 0, N-1)

    else:
        res.append(query(1, 0, N-1, b-1, a-1))

for elem in res:
    print(elem)