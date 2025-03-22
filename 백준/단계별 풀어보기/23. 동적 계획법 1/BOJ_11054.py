n = int(input())
seq = list(map(int, input().split()))
dp_inc = [1]*n
dp_dec = [1]*n
ans = 0
for i in range(n):
    for j in range(i, n):
        if seq[j] > seq[i]:
            dp_inc[j] = max(dp_inc[i] + 1, dp_inc[j])
seq.reverse()
for i in range(n):
    for j in range(i, n):
        if seq[j] > seq[i]:
            dp_dec[j] = max(dp_dec[i] + 1, dp_dec[j])
dp_dec.reverse()

for i in range(n):
    if dp_inc[i] + dp_dec[i] > ans:
        ans = dp_inc[i] + dp_dec[i]

print(ans - 1)