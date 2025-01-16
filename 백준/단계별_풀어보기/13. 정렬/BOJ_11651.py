n = int(input())
coor = []
for _ in range(n):
    x, y = map(int, input().split())
    coor.append([x, y])
coor.sort(key = lambda x : (x[1], x[0]))
for c in coor:
    print(*c)