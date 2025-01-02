import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
N_arr = [list(map(int, input().split())) for _ in range(N)]
soil = [[[5, [], [], []] for _ in range(N)] for _ in range(N)]  # [양분, 현재나무, 임시나무, 죽은나무]
M_arr = [list(map(int, input().split())) for _ in range(M)]
dydx = [[-1, 1], [-1, -1], [-1, 0], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]


def spring(soil):
    for i in range(N):
        for j in range(N):
            food, current, temp, dead = soil[i][j]
            current.sort()  # 나이 순으로 정렬

            for age in current:
                if food >= age:
                    food -= age
                    temp.append(age + 1)
                else:
                    dead.append(age)

            current = temp
            temp = []
            soil[i][j] = [food, current, temp, dead]

    return soil


def summer(soil):
    for i in range(N):
        for j in range(N):
            food, current, temp, dead = soil[i][j]

            while dead:
                food += dead.pop() // 2

            soil[i][j] = [food, current, temp, []]

    return soil


def fall(soil):
    for i in range(N):
        for j in range(N):
            food, current, temp, dead = soil[i][j]
            if current:
                for age in current:
                    if age % 5 == 0:
                        for dy, dx in dydx:
                            _i, _j = i + dy, j + dx
                            if 0 <= _i < N and 0 <= _j < N:
                                soil[_i][_j][1].append(1)

    return soil


def winter(soil):
    for i in range(N):
        for j in range(N):
            soil[i][j][0] += N_arr[i][j]

    return soil

for r, c, age in M_arr:
    soil[r-1][c-1][1].append(age)

for _ in range(K):
    soil = spring(soil)
    soil = summer(soil)
    soil = fall(soil)
    soil = winter(soil)

total = sum(len(soil[i][j][1]) for i in range(N) for j in range(N))
print(total)