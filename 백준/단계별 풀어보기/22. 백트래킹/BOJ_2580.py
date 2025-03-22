def check_row(num, x):
    if num in sudoku[x]:
        return False
    return True

def check_col(num, y):
    for i in range(9):
        if num == sudoku[i][y]:
            return False
    return True
    
def check_square(num, area_x, area_y):
    for i in range(area_x, area_x+3):
        for j in range(area_y, area_y+3):
            if sudoku[i][j] == num:
                return False
    return True

def possible_nums(x, y):
    nums = []
    area_x = (x // 3)*3
    area_y = (y // 3)*3
    for num in range(1, 10):
        if check_row(num, x) and check_col(num, y) and check_square(num, area_x, area_y):
            nums.append(num)
    return nums
        
def sudoku_sol(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                nums = possible_nums(i, j)
                if not nums:
                    return False
                for n in nums:
                    sudoku[i][j] = n
                    if sudoku_sol(sudoku):
                        return True
                sudoku[i][j] = 0
                return False
    return sudoku

sudoku = [list(map(int, input().split())) for _ in range(9)]
sudoku_sol(sudoku)
for s in sudoku:
    print(*s)