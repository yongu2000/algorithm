# https://school.programmers.co.kr/learn/courses/30/lessons/84021

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = 0, 0
visited = []

def bfs(graph, path, x, y):
    global n, m, visited

    queue = deque()
    visited[x][y] = True
    queue.append([x, y])

    data = [[0] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()

        data[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == path:
                visited[nx][ny] = True
                queue.append([nx, ny])
    return data

def align(block):

    most_up = n+1
    most_left = m+1

    for i in range(n):
        for j in range(m):
            if block[i][j] == 1:
                most_up = min(most_up, i)
                most_left = min(most_left, j)

    data = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if block[i][j] == 1:
                data[i - most_up][j - most_left] = 1

    return data

def rotate(block):

    data = [[[0] * m for _ in range(n)] for _ in range(4)]

    for i in range(n):
        for j in range(m):
            if block[i][j] == 1:
                data[0][i][j] = 1
                data[1][n-1-j][i] = 1
                data[2][j][n-1-i] = 1
                data[3][n-1-i][n-1-j] = 1

    aligned = []
    for d in data:
        aligned.append(align(d))
    return aligned

def solution(game_board, table):
    global n, m, visited
    n = len(game_board)
    m = len(game_board[0])
    
    slots = []
    blocks = []

    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and game_board[i][j] == 0:
                slots.append(bfs(game_board, 0, i, j))

    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and table[i][j] == 1:
                blocks.append(bfs(table, 1, i, j))
    
    slots_aligned = []
    for slot in slots:
        slots_aligned.append(align(slot))

    blocks_rotated_aligned = []
    for block in blocks:
        blocks_rotated_aligned.append(rotate(block))

    used = [False] * len(blocks_rotated_aligned)
    
    answer = 0
    
    for slot in slots_aligned:
        for idx, rotated_blocks in enumerate(blocks_rotated_aligned):
            if used[idx]:
                continue
            for block in rotated_blocks:
                if block == slot:
                    for s in slot:
                        answer += sum(s)
                    used[idx] = True
                    break
            if used[idx]:
                break
    return answer

# print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
#                , [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
# print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))

print(solution([
    [0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0],
    [1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1],
    [0,1,1,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0],
    [0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0],
    [0,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1],
    [1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0],
    [0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,1],
    [1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0],
    [0,0,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0],
    [1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1],
    [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0],
    [1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0],
    [0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0],
    [1,0,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0],
    [0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0],
    [0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0],
    [0,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,1,0]
], [[1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0],
    [0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0],
    [1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,1,0,1],
    [1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,1],
    [1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1],
    [0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0],
    [1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1],
    [0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0],
    [1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0],
    [1,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,0],
    [0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1],
    [1,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1],
    [1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1],
    [0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0],
    [1,1,1,0,1,0,0,1,0,1,1,0,0,1,0,1,0,1],
    [0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,1],
    [0,1,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1]]))

