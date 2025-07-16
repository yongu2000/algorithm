# https://school.programmers.co.kr/learn/courses/30/lessons/17679

answer = 0

def check(board, visited, i, j):
    global answer
    standard = board[i][j]
    if standard == " ":
        return False

    if board[i+1][j] == standard and board[i][j+1] == standard and board[i+1][j+1] == standard:
        for x in range(2):
            for y in range(2):
                answer += 1 if visited[i+x][j+y] == False else 0
                visited[i+x][j+y] = True
        return True
    return False

def solution(m, n, board):
    global answer
    answer = 0
    board = list(list(b) for b in board)
    broke = True

    while broke:
        broke = False
        visited = [[False]*n for _ in range(m)] 
        for i in range(m-1):
            for j in range(n-1):
                if check(board, visited, i, j):
                    broke = True
        
        # break_block()
        for i in range(m):
            for j in range(n):
                if visited[i][j] == True:
                    board[i][j] = " "

        # align()
        new_board = [[" "]*n for _ in range(m)]
        for j in range(n-1, -1, -1):
            blank_last = -1
            blank_count = 0
            for i in range(m-1, -1, -1):
                if board[i][j] == " ":
                    blank_last = i
                    blank_count += 1
                elif blank_last > i:
                    blank_last = i
                    new_board[i+blank_count][j] = board[i][j]
                else:
                    new_board[i][j] = board[i][j]
        board = new_board
                
    return answer

print(solution(4, 5, 	["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 5
print(solution(6, 6, 		["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 5



