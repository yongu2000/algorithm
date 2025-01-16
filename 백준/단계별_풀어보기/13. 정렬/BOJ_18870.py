n = int(input())
nums = list(map(int, input().split()))
zip_nums = dict()
ans = list()
for i, num in enumerate(sorted(list(set(nums)))):
    zip_nums[num] = i
for num in nums:
    ans.append(zip_nums[num])
print(*ans)