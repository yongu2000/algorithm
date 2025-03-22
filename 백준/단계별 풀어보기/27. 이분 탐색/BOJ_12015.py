import sys
from bisect import bisect_left
input = sys.stdin.readline

def my_bisect(num, nums):
    start = 0
    end = len(nums) - 1 

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == num:
            return mid
        elif nums[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return start

# solve 1
n = int(input())
nums = list(map(int, input().split()))
ans = [nums[0]]

for num in nums:
    if ans[-1] < num:
        ans.append(num)
    else:
        idx = my_bisect(num, ans)
        ans[idx] = num
    
print(len(ans))

# # solve 2 bisect 라이브러리리 활용
# for num in nums:
#     if ans[-1] < num:
#         ans.append(num)
#     else:
#         idx = bisect_left(ans, num)
#         ans[idx] = num
    
# print(ans)