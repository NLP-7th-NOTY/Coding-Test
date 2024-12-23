sudoku = [list(map(int, input().split())) for _ in range(9)]
empty = []

def get_candidate(sudoku, i, j):
    used = set(sudoku[i])
    used.update(row[j] for row in sudoku)
    dy, dx = i // 3 * 3, j // 3 * 3
    used.update(sudoku[y][x] for y in range(dy, dy + 3) for x in range(dx, dx + 3))  # 3x3 박스
    return set(range(1, 10)) - used

def DFS(sudoku, empty):
    if len(empty) == 0:
        for elem in sudoku:
            print(str(elem)[1:-1].replace(',',''))
        return True

    elem = empty[0]
    i, j = elem
    candidate_list = get_candidate(sudoku, i, j)
    for candidate in candidate_list:
        sudoku[i][j] = candidate
        if DFS(sudoku, empty[1:]):
            return True

        sudoku[i][j] = 0
    return False

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empty.append([i,j])

DFS(sudoku, empty)