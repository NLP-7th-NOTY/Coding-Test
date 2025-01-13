r, c, k = map(int, input().split())
ipt = [list(map(int, input().split())) for _ in range(3)]
arr = [[0]*100 for _ in range(100)]
row_mapper = [dict() for _ in range(100)]
col_mapper = [dict() for _ in range(100)]
t = 0
row, col = 3, 3

for i in range(3):
    for j in range(3):
        arr[i][j] = ipt[i][j]

if arr[r-1][c-1] == k:
    print(0)
    exit()

while t != 100:
    if row >= col:
        m_col = -1
        for i in range(row):
            row_mapper[i] = {}
            for elem in arr[i]:
                if elem in row_mapper[i]:
                    row_mapper[i][elem] += 1

                else:
                    row_mapper[i][elem] = 1

            f = []
            for elem in row_mapper[i]:
                if elem != 0:
                    f.append([elem, row_mapper[i][elem]])

            f = sorted(f, key=lambda x : (x[1], x[0]))

            arr[i] = []
            for _ in range(len(f)):
                for elem in f[_]:
                    arr[i].append(elem)

            m_col = max(m_col, len(arr[i]))

        for i in range(row):
            arr[i].extend([0 for _ in range(100 - len(arr[i]))])

        if arr[r-1][c-1] == k:
            print(t+1)
            exit()

        col = m_col
        t += 1

    else:
        m_row = -1
        for i in range(col):
            col_mapper[i] = {}
            for elem in list(zip(*arr))[i]:
                if elem in col_mapper[i]:
                    col_mapper[i][elem] += 1

                else:
                    col_mapper[i][elem] = 1

            f = []
            for elem in col_mapper[i]:
                if elem != 0:
                    f.append([elem, col_mapper[i][elem]])

            f = sorted(f, key=lambda x : (x[1], x[0]))

            temp = []
            for _ in range(len(f)):
                for elem in f[_]:
                    temp.append(elem)

            for j in range(len(temp)):
                arr[j][i] = temp[j]

            for _ in range(j+1, 100):
                arr[_][i] = 0

            m_row = max(m_row, len(temp))

        if arr[r-1][c-1] == k:
            print(t+1)
            exit()

        row = m_row
        t += 1

print(-1)