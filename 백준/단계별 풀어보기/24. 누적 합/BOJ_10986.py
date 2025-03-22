import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * (n+1) 
mods = [0] * (k+1)

ans = 0

# for i in range(1, n+1):
#     for j in range(i, n+1):
#         if (sums[j] - sums[j-i]) % k == 0:
# ---> sums[j] % k = sums[j-i] % k
# ---> mods[j] = mods[j-i]
# 즉 mods중 값이 같은 2개의 index를 고르는 경우의 수 nC2
# 공식 = n * (n-1) // 2 

for i in range(1, n+1):
    sums[i] = sums[i-1] + nums[i-1]
    mods[sums[i] % k] += 1
ans += mods[0]
for i in range(k):
    ans += mods[i] * (mods[i]-1) // 2

print(ans)