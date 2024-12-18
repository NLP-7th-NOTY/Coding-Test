N = int(input())

dydx = [[0,1], [-1,0], [0,-1], [1,0]]
arr = [list(map(int, input().split(' '))) for _ in range(N)]
grid = [[0] * 101 for _ in range(101)]

for elem in arr:
    x, y, d, g = elem
    curve_id = [d]

    for i in range(g):
        curve_id += [(i+1)%4 for i in curve_id[::-1]]

    grid[y][x] = 1
    for elem in curve_id:
        y, x = y + dydx[elem][0], x + dydx[elem][1]
        grid[y][x] = 1

print(sum(grid[i][j] and grid[i + 1][j] and grid[i][j + 1] and grid[i + 1][j + 1] for i in range(100) for j in range(100)))