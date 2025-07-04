# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    sums = [[0] *(m+1) for _ in range(n+1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            sums[r1][c1] -= degree
            sums[r1][c2+1] -= -degree
            sums[r2+1][c1] -= -degree
            sums[r2+1][c2+1] -= degree
        else:
            sums[r1][c1] += degree
            sums[r1][c2+1] += -degree
            sums[r2+1][c1] += -degree
            sums[r2+1][c2+1] += degree

    for i in range(n):
        for j in range(m+1):
            sums[i+1][j] += sums[i][j]
    
    for i in range(n+1):
        for j in range(m):
            sums[i][j+1] += sums[i][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += sums[i][j]

    for row in board:
        for val in row:
            if val > 0:
                answer += 1
    
    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
               )) 
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
               [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
               )) 
