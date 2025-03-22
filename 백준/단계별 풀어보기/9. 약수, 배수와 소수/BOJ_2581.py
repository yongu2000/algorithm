m = int(input())
n = int(input())

ans = []
for num in range(m, n+1):
    for i in range(2, num+1):
        if num % i == 0:
            if (i == num):
                ans.append(i)
            break
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))