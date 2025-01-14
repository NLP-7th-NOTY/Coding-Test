N = int(input())
like = [list(map(int, input().split())) for _ in range(N**2)]
arr = [[0 for _ in range(N)] for _ in range(N)]
dydx = [[-1,0],[1,0],[0,-1],[0,1]]
id_to_idx_mapper = {}

for i in range(N**2):
    id_to_idx_mapper[like[i][0]] = i

def get_score(idx, d1):
    y,x = d1
    like_idx = like[id_to_idx_mapper[idx]]
    score = 0
    for elem in dydx:
        _y, _x = y + elem[0], x + elem[1]
        if 0 <= _y < N and 0 <= _x < N and arr[_y][_x] in like_idx[1:]:
            score += 1

    return 10 ** (score-1) if score >= 1 else 0

def search(idx, d1):
    y,x = d1
    like_idx = like[idx]
    n_like, n_empty = 0, 0
    for elem in dydx:
        _y, _x = y + elem[0], x + elem[1]
        if 0 <= _y < N and 0 <= _x < N:
            if arr[_y][_x] in like_idx[1:]:
                n_like += 1

            elif arr[_y][_x] == 0:
                n_empty += 1

    return [n_like, n_empty]

def curriculum():
    for id, elem in enumerate(like):
        idx = elem[0]

        empty_candidate = []
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    result = search(id, [i,j])
                    result.extend([i,j])
                    empty_candidate.append(result)

        empty_candidate = sorted(empty_candidate, key=lambda x : (x[0], x[1], -x[2], -x[3]))
        _, _, y,x = empty_candidate.pop()
        arr[y][x] = idx

curriculum()
res = 0
for i in range(N):
    for j in range(N):
        res += get_score(arr[i][j], [i,j])

print(res)