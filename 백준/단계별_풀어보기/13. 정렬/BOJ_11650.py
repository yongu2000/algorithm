n = int(input())
coor = []
for _ in range(n):
    x, y = map(int, input().split())
    coor.append([x, y])
coor.sort()
for c in coor:
    print(*c)