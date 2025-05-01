import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

answer = 0
for i in range(n):
    target = nums[i]
    left = 0
    right = n-1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            if i != left and i != right:
                answer += 1
                break
            elif i == left:
                left += 1
            else:
                right -= 1

print(answer)
