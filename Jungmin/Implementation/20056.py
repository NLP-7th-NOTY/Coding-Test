import math

N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(M)]
grid = [[0 for _ in range(N)] for _ in range(N)]
overlap = [[-1 for _ in range(N)] for _ in range(N)]
dir_dydx = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

def next_location(y, x, s, d):
    _y, _x = dir_dydx[d]
    return (y+_y * s) % N, (x+_x * s) % N

def command(fireball):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    overlap = [[-1 for _ in range(N)] for _ in range(N)]

    cmd = []
    two_fireball = []
    next_fireball = []

    for elem in fireball:
        y,x,m,s,d = elem
        _y, _x = next_location(y, x, s, d)

        cmd.append([_y,_x,m,s,d,1])

        if d % 2 == 0:
            cmd[-1].extend([True, None])

        else:
            cmd[-1].extend([None, True])

    for elem in cmd:
        y, x, m, s, d, c, even, odd = elem

        if overlap[y][x] == -1:
            overlap[y][x] = 0
            grid[y][x] = [m, s, d, c, even, odd]

        elif overlap[y][x] == 0:
            two_fireball.append([y, x])

            grid[y][x][0] += m
            grid[y][x][1] += s
            grid[y][x][2] += d
            grid[y][x][3] += 1

            if d % 2 == 0:
                grid[y][x][4] = True

            else:
                grid[y][x][5] = True

    for elem in two_fireball:
        y, x = elem

        if isinstance(grid[y][x], list):
            m, s, d, c, even, odd = grid[y][x]
            sep_mass = math.floor(m/5)

            if sep_mass != 0:
                sep_vel = math.floor(s / c)

                if even is None or odd is None:
                    next_fireball.append([y, x, sep_mass, sep_vel, 0])
                    next_fireball.append([y, x, sep_mass, sep_vel, 2])
                    next_fireball.append([y, x, sep_mass, sep_vel, 4])
                    next_fireball.append([y, x, sep_mass, sep_vel, 6])

                else:
                    next_fireball.append([y, x, sep_mass, sep_vel, 1])
                    next_fireball.append([y, x, sep_mass, sep_vel, 3])
                    next_fireball.append([y, x, sep_mass, sep_vel, 5])
                    next_fireball.append([y, x, sep_mass, sep_vel, 7])

        overlap[y][x] = -1
        grid[y][x] = 0

    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0 and overlap[i][j] == 0:
                m,s,d = grid[i][j][0], grid[i][j][1], grid[i][j][2]
                next_fireball.append([i,j,m,s,d])

    return next_fireball


for i in range(M):
    fireball[i][0] -= 1
    fireball[i][1] -= 1

for i in range(K):
    fireball = command(fireball)

res = 0
for elem in fireball:
    res += elem[2]

print(res)