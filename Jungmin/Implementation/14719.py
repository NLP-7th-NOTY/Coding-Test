H, W = map(int, input().split(' '))
rain = list(map(int, input().split(' ')))
block = [[0] * W for _ in range(H)]
tot = 0
start = -1

for i, elem in enumerate(rain):
    for j in range(elem):
        block[j][i] = 1

for i in range(H):
    for j in range(W):
        if block[i][j] == 1 and start == -1:
            start = j

        elif block[i][j] == 1 and start != -1:
            tot += list(block[i][start:j]).count(0)
            start = j

print(tot)