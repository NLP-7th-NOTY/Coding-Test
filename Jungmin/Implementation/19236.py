import copy

arr = [list(map(int, input().split())) for _ in range(4)]
grid = [[0 for _ in range(4)] for _ in range(4)]

dir_dydx = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
dydx = [[-1,0],[1,0],[0,-1],[0,1]]

def find_fish(grid, n_fish):
    for i in range(4):
        for j in range(4):
            if isinstance(grid[i][j], list) and grid[i][j][0] == n_fish:
                return [i,j]

    return None

def move(grid, yx, dir_num):
    y, x = yx
    start_dir = dir_num

    n_fish = grid[y][x][0]

    for i in range(0, 8):
        _dir = (start_dir - 1 + i) % 8
        dy, dx = dir_dydx[_dir]
        _y, _x = y + dy, x + dx

        if 0 <= _y < 4 and 0 <= _x < 4:
            if grid[_y][_x] == -1:
                grid[_y][_x] = [n_fish, _dir+1]
                grid[y][x] = -1

                return

            elif isinstance(grid[_y][_x], list) and grid[_y][_x][0] != -1:
                n_fish, _ = grid[y][x]
                t_fish, t_dir = grid[_y][_x]

                grid[y][x] = [t_fish, t_dir]
                grid[_y][_x] = [n_fish, _dir+1]

                return

def day(grid, shark_info):
    for i in range(16):
        cord = find_fish(grid, i+1)

        if cord is not None:
            fish_dir = grid[cord[0]][cord[1]][1]
            move(grid, cord, fish_dir)

    eat_fish_candidate = []
    s_y, s_x, s_d = shark_info
    dy, dx = dir_dydx[s_d - 1]
    for i in range(1, 4):
        ny = s_y + dy * i
        nx = s_x + dx * i

        if 0 <= ny < 4 and 0 <= nx < 4 and isinstance(grid[ny][nx], list):
            eat_fish_candidate.append([ny, nx])

    return shark_info, eat_fish_candidate


def DFS(grid, shark_info, eat_fish_rank):
    shark_info, eat_fish_candidate = day(grid, shark_info)
    s_y, s_x, s_d = shark_info

    if not eat_fish_candidate:
        global res
        res = max(res, eat_fish_rank)
        return

    for elem in eat_fish_candidate:
        y, x = elem
        n_fish, n_dir = grid[y][x]
        grid[y][x] = [-1, n_dir]
        grid[s_y][s_x] = -1

        t_grid = copy.deepcopy(grid)

        DFS(t_grid, [y, x, n_dir], eat_fish_rank+n_fish)

        grid[s_y][s_x] = [-1, s_d]
        grid[y][x] = [n_fish, n_dir]


next_fish_heap = []
for i in range(4):
    for j in range(4):
        grid[i][j] = [arr[i][2*j], arr[i][2*j+1]]

res = grid[0][0][0]
grid[0][0][0] = -1
shark_info = [0, 0, grid[0][0][1]]
eat_fish_candidate = []
DFS(grid, shark_info, res)
print(res)