from itertools import combinations

N, M, H = map(int, input().split())
grid = [[0]*(2*N-1) for _ in range(H+2)]
candidate = []

def get_end(grid):
    for i in range(0, 2*N-1, 2):
        current = i
        for y in range(1, H+2):
            if current < 2*N-2 and grid[y][current+1] == 1:
                current += 2
            elif current > 0 and grid[y][current-1] == 1:
                current -= 2
        if current != i:
            return False
    return True

for i in range(H+2):
    for j in range(2*N):
        if j % 2 == 0:
            grid[i][j] = 1

for i in range(M):
    a, b = map(int, input().split(' '))
    y, x = a, (b-1) * 2 + 1
    grid[y][x] = 1

for i in range(1, len(grid)-1):
    for j in range(len(grid[i])):
        if j % 2 == 1 and grid[i][j] == 0:
            candidate.append([i,j])

filtered_candidates = []
for y, x in candidate:
    if x > 1 and grid[y][x-2] == 1:
        continue
    if x < 2*N-3 and grid[y][x+2] == 1:
        continue
    filtered_candidates.append([y, x])

for r in range(0, 4):
    arr = combinations(filtered_candidates, r)

    for elem in arr:
        for eelm in elem:
            y, x = eelm
            grid[y][x] = 1

        if get_end(grid):
            print(r)
            exit()

        for eelm in elem:
            y, x = eelm
            grid[y][x] = 0

print(-1)