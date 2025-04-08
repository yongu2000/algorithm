import sys
input = sys.stdin.readline

def is_heart(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    heart = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and cookie[nx][ny] == "*":
            heart += 1
        else:
            break
    if heart == 4:
        return True
    return False

def find_body(heart):
    waist, left_leg, right_leg = find_waist(heart)
    return find_left_arm(heart), find_right_arm(heart), waist, left_leg, right_leg
    

def find_left_arm(heart):
    x, y = heart
    length = 0
    while True:
        y -= 1
        if 0 <= x < n and 0 <= y < n and cookie[x][y] == "*":
            length += 1
        else:
            break
    return length

def find_right_arm(heart):
    x, y = heart
    length = 0
    while True:
        y += 1
        if 0 <= x < n and 0 <= y < n and cookie[x][y] == "*":
            length += 1
        else:
            break
    return length

def find_waist(heart):
    x, y = heart
    lenght = 0
    while True:
        x += 1
        if 0 <= x < n and 0 <= y < n and cookie[x][y] == "*":
            lenght += 1
        else:
            break
    return lenght, find_left_leg([x, y]), find_right_leg([x, y])

def find_left_leg(waist):
    x, y = waist
    x -= 1
    y -= 1
    length = 0
    while True:
        x += 1
        if 0 <= x < n and 0 <= y < n and cookie[x][y] == "*":
            length += 1
        else:
            break
    
    return length

def find_right_leg(waist):
    x, y = waist
    x -= 1
    y += 1
    length = 0
    while True:
        x += 1
        if 0 <= x < n and 0 <= y < n and cookie[x][y] == "*":
            length += 1
        else:
            break
    
    return length

n = int(input())
cookie = [list(input().strip()) for _ in range(n)]
heart = []
for i in range(n):
    for j in range(n):
        if is_heart(i, j):
            heart = [i, j]
            break
    if heart:
        break

print(heart[0]+1, heart[1]+1)
print(*find_body(heart))
