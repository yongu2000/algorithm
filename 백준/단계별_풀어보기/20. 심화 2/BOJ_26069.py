import sys
input = sys.stdin.readline

n = int(input())
rainbow = set(['ChongChong'])
for _ in range(n):
    a, b = list(input().split())
    if a in rainbow or b in rainbow:
        rainbow.add(a)
        rainbow.add(b)

print(len(rainbow))