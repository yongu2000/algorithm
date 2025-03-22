import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(q):
    queue = deque(q)

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append([nx, ny, nz])

def find_min(data):
    min_num = sys.maxsize
    for dat in data:
        for da in dat:
            for d in da:
                if min_num > d:
                    min_num = d
    return min_num

def find_max(data):
    max_num = -sys.maxsize
    for dat in data:
        for da in dat:
            for d in da:
                if max_num < d:
                    max_num = d
    return max_num

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                queue.append([i, j, k])
            if box[k][i][j] == -1:
                box[k][i][j] = 1
bfs(queue)

if find_min(box) == 0:
    print(-1)
else:
    print(find_max(box) - 1)

