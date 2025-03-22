import sys
input = sys.stdin.readline

def color_board(i, j):
    if board[i-1][j-1] == "B":
        if i % 2 == 0 and j % 2 == 0:
            black[i][j] = 0 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
            white[i][j] = 1 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
        elif i % 2 == 0 and j % 2 != 0:
            black[i][j] = 1 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
            white[i][j] = 0 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
        elif i % 2 != 0 and j % 2 == 0:
            black[i][j] = 1 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
            white[i][j] = 0 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
        elif i % 2 != 0 and j % 2 != 0:
            black[i][j] = 0 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
            white[i][j] = 1 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
    elif board[i-1][j-1] == "W":
        if i % 2 == 0 and j % 2 == 0:
            black[i][j] = 1 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
            white[i][j] = 0 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
        elif i % 2 == 0 and j % 2 != 0:
            black[i][j] = 0 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
            white[i][j] = 1 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
        elif i % 2 != 0 and j % 2 == 0:
            black[i][j] = 0 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
            white[i][j] = 1 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]
        elif i % 2 != 0 and j % 2 != 0:
            black[i][j] = 1 + black[i-1][j] + black[i][j-1] - black[i-1][j-1]
            white[i][j] = 0 + white[i-1][j] + white[i][j-1] - white[i-1][j-1]

def color_needed(b, i, j):
    return b[i+k][j+k] - b[i][j+k] - b[i+k][j] + b[i][j]

n, m, k = map(int, input().split())
board = list(list(input().strip()) for _ in range(n))
black = [[0]*(m+1) for _ in range(n+1)]
white = [[0]*(m+1) for _ in range(n+1)]
answer = sys.maxsize

for i in range(1, n+1):
    for j in range(1, m+1):
        color_board(i, j)

for i in range(n - k + 1):
    for j in range(m - k + 1):
        answer = min(answer, color_needed(black, i, j), color_needed(white, i, j))
print(answer)
