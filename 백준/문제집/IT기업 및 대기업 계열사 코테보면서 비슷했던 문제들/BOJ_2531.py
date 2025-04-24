import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushis = []
for _ in range(n):
    sushis.append(int(input()))
sushis.extend(sushis[:k-1])

max_sushi = -1

for i in range(n):
    temp = set(sushis[i:i+k])
    coupon = 1 if c not in temp else 0
    max_sushi = max(max_sushi, len(temp) + coupon)

print(max_sushi)    