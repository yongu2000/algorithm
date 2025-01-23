def hanoi(n, start, mid, to):
    if n == 1:
        ans.append([start, to])
        return
    hanoi(n-1, start, to, mid)
    ans.append([start, to])
    hanoi(n-1, mid, start, to)
        
n = int(input())
ans = []
hanoi(n, 1, 2, 3)
print(*ans)