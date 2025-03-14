import sys
input = sys.stdin.readline

def mean():
    print(round(sum(nums)/len(nums)))

def median():
    print(nums[len(nums)//2])

def mode():
    counts = {}
    ans = []
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_val = -sys.maxsize

    for val in counts.values():
        if val > max_val:
            max_val = val
    
    for key, val in counts.items():
        if val == max_val:
            ans.append(key)

    if len(ans) != 1:
        print(ans[1])
    else:
        print(ans[0])

def domain():
    print(nums[-1] - nums[0])

n = int(input())
nums = sorted([int(input()) for _ in range(n)])
mean()
median()
mode()
domain()