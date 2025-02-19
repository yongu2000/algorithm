import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0
coins = []
for _ in range(n):
    coins.append(int(input())) 

coins.reverse()
for c in coins:
    if c <= k:
        num = k // c
        k -= c*num
        ans += num
print(ans)
