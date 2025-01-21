import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Marr = [list(map(int, input().split())) for _ in range(M)]

dir_dydx = [[0, 0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
bucket_dydx = [[-1,-1],[-1,1],[1,-1],[1,1]]
cloud_mapper = {}

def move(before, dir, length):
    next_y, next_x = before[0] + (dir_dydx[dir][0] * length), before[1] + (dir_dydx[dir][1] * length)
    return [next_y % N, next_x % N]

def day(today_dir, today_len, cloud_location):
    for i in range(len(cloud_location)):
        cloud_location[i] = move(cloud_location[i], today_dir, today_len)

    for elem in cloud_location:
        cloud_mapper[f'{elem[0]}_{elem[1]}'] = 1
        y, x = elem
        arr[y][x] += 1

    add_water = []
    for elem in cloud_location:
        n_this_location_water = 0
        y, x = elem
        for dydx in bucket_dydx:
            _y, _x = y + dydx[0], x + dydx[1]
            if 0 <= _y < N and 0 <= _x < N and arr[_y][_x] > 0:
                n_this_location_water += 1

        add_water.append(n_this_location_water)

    for i in range(len(cloud_location)):
        y,x = cloud_location[i][0], cloud_location[i][1]
        arr[y][x] += add_water[i]

    next_day_cloud_location = []
    for i in range(N):
        for j in range(N):
            if f'{i}_{j}' not in cloud_mapper and arr[i][j] >= 2:
                arr[i][j] -= 2
                next_day_cloud_location.append([i,j])

    return next_day_cloud_location

cloud_location = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for i in range(M):
    today_dir, today_len = Marr[i]
    cloud_location = day(today_dir, today_len, cloud_location)
    cloud_mapper.clear()

print(sum(sum(arr, [])))