import sys
input = sys.stdin.readline

n = int(input())
rooms = []
for _ in range(n):
    s, e = map(int, input().split())
    rooms.append([s, e])
rooms.sort(key = lambda x : (x[1], x[0]))

end = -1
ans = 0
for r in rooms:
    s, e = r
    if s >= end:
        end = e
        ans += 1
print(ans)