import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medals = []
target_medal = []

for _ in range(n):
    i, g, s, b = map(int, input().split())
    medals.append([g, s, b])
    if i == k:
        target_medal = [g, s, b]

sorted_medals = sorted(medals, key = lambda x : (x[0], x[1], x[2]), reverse=True)

print(sorted_medals.index(target_medal)+1)
