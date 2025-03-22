n = int(input())
nums = list(map(int, input().split()))
ans = []
for num in nums:
    for i in range(2, num+1):
        if num % i == 0:
            if (i == num):
                ans.append(num)
            break
print(len(ans))