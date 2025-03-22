import sys
input = sys.stdin.readline

n = int(input())

box = 1
ans = 1

while box < n:
    box += 6 * ans
    ans += 1
print(ans)