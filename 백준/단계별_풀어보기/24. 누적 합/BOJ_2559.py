import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
sums = [0]
answer = -10**7 - 1

for i in range(1, n+1):
    sums.append(sums[i-1] + temp[i-1])
for i in range(k, n+1):
    answer = max(answer, sums[i]-sums[i-k])
print(answer)