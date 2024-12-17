N, M = map(int, input().split(' '))
paper = [list(map(int, input().split(' '))) for _ in range(N)]
tot = sum(paper[i].count(1) for i in range(N))
day = 0
dydx = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def BFS(x, y, check):
    stack = [[y,x]]
    while stack:
        y, x = stack.pop()
        check[y][x] = -1

        for elem in dydx:
            new_y = y + elem[0]
            new_x = x + elem[1]

            if 0 <= new_y < N and 0 <= new_x < M and check[new_y][new_x] == 0:
                stack.append([new_y, new_x])

    return check

while tot:
    paper = BFS(0, 0, paper)

    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1:
                is_near_air = 0

                for elem in dydx:
                    new_y = i + elem[0]
                    new_x = j + elem[1]

                    if 0 <= new_y < N and 0 <= new_x < M and paper[new_y][new_x] == -1:
                        is_near_air += 1

                        if is_near_air >= 2:
                            paper[i][j] = 0
                            tot -= 1
                            break

    for i in range(N):
        for j in range(M):
            if paper[i][j] != 1:
                paper[i][j] = 0

    day += 1

print(day)