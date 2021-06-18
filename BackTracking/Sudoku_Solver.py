
def isSudokuValid(sudoku):

    row = [dict() for i in range(9)]
    col = [dict() for i in range(9)]
    subGrid = [[dict() for i in range(3)] for i in range(3)]

    for r in range(9):
        for c in range(9):

            if (sudoku[r][c] == 0):
                continue

            if (sudoku[r][c] in subGrid[r//3][c//3] or sudoku[r][c] in col[c] or sudoku[r][c] in row[r]):
                return False

            subGrid[r//3][c//3][sudoku[r][c]] = True
            row[r][sudoku[r][c]] = True
            col[c][sudoku[r][c]] = True

    return True


sudoku = [[int(ele) for ele in input().split()]for i in range(9)]
ans = isSudokuValid(sudoku)
if ans is True:
    print('true')
else:
    print('false')
