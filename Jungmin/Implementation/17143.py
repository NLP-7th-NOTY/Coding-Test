def move_shark(r, c, s, d, R, C):
    if d == 1 or d == 2:
        cycle = 2 * (R - 1)
        s %= cycle
        if d == 1:
            r -= s
            if r < 1:
                r = 2 - r
                d = 2
            if r > R:
                r = 2 * R - r
                d = 1
        else:
            r += s
            if r > R:
                r = 2 * R - r
                d = 1
            if r < 1:
                r = 2 - r
                d = 2
    else:
        cycle = 2 * (C - 1)
        s %= cycle
        if d == 4:
            c -= s
            if c < 1:
                c = 2 - c
                d = 3
            if c > C:
                c = 2 * C - c
                d = 4
        else:
            c += s
            if c > C:
                c = 2 * C - c
                d = 4
            if c < 1:
                c = 2 - c
                d = 3
    return r, c, d

def solution(R, C, M, sharks):
    board = [[0] * (C + 1) for _ in range(R + 1)]
    for r, c, s, d, z in sharks:
        board[r][c] = (s, d, z)

    total_size = 0
    for fisher in range(1, C + 1):
        for i in range(1, R + 1):
            if board[i][fisher]:
                total_size += board[i][fisher][2]
                board[i][fisher] = 0
                break

        new_board = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if board[r][c]:
                    s, d, z = board[r][c]
                    nr, nc, nd = move_shark(r, c, s, d, R, C)
                    if new_board[nr][nc] == 0 or new_board[nr][nc][2] < z:
                        new_board[nr][nc] = (s, nd, z)
        board = new_board

    return total_size

R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]

print(solution(R, C, M, sharks))
