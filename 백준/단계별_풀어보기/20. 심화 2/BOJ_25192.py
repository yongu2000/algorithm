import sys
input = sys.stdin.readline

n = int(input())
gomgom = []
ans = 0
for _ in range(n):
    chat = input().strip()
    if chat == "ENTER":
        gomgom.append(set())
    else:
        gomgom[-1].add(chat)
for g in gomgom:
    ans += len(g)
print(ans)