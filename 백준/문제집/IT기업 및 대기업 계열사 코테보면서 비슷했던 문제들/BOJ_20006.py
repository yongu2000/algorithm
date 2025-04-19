import sys
input = sys.stdin.readline

p, m = map(int, input().split())

rooms = []
for _ in range(p):
    level, n = input().strip().split()
    l = int(level)
    if not rooms:
        rooms.append([[l, n]])
    else:
        joined = False
        for r in rooms:
            if len(r) >= 1 and ((r[0][0] - 10) <= l <= (r[0][0] + 10)) and len(r) < m:
                r.append([l, n])
                joined = True
                break
        if not joined:
            rooms.append([[l, n]])
for r in rooms:
    r.sort(key = lambda x: x[1])

for r in rooms:
    if len(r) == m:
        print("Started!")
        for player in r:
            print(player[0], player[1])
    else:
        print("Waiting!")
        for player in r:
            print(player[0], player[1])