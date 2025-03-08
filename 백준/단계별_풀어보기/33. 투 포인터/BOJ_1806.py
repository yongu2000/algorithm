import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]
for i in range(len(nums)):
    sums.append(nums[i]+sums[i])

print(sums)
left = 1
right = 1
ans = sys.maxsize
possible = False
while True:
    temp = sums[right] - sums[left-1]
    if temp >= s:
        ans = min(ans, right-left+1)
        possible = True
        left += 1
    elif right == n:
        break
    else:
        right += 1

if possible:
    print(ans)
else:
    print(0)