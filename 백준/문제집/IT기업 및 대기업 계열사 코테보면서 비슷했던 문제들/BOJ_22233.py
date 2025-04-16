import sys
input = sys.stdin.readline

n, m = map(int, input().split())

keywords = dict()
for _ in range(n):
    keywords[input().strip()] = 1

for _ in range(m):
    blog = list(input().strip().split(","))
    for k in blog:
        keywords.pop(k, None)
    print(len(keywords.keys()))
