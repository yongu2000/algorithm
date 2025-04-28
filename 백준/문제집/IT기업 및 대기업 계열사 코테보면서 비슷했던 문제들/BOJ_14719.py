import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = [[0]*w for _ in range(h)]

data = list(map(int, input().split()))

for i in range(w):
    for j in range(data[i]):
        blocks[j][i] = 1

answer = 0
for i in range(h):
    count = 0
    left, right = 0, w-1
    has_left, has_right = False, False
    for j in range(w):
        if blocks[i][j] == 1:
            left = j
            has_left = True
            break
    for j in range(w-1, -1, -1):
        if blocks[i][j] == 1:
            right = j
            has_right = True
            break

    for j in range(left, right):
        if has_left and has_right and blocks[i][j] == 0:
            count += 1
    answer += count

print(answer)