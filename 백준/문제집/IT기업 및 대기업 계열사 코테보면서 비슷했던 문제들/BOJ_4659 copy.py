import sys
input = sys.stdin.readline

n = int(input())
buildings = [0] + list(map(int, input().split()))

ans = []
for i in range(1, n+1):
    temp = []

    max_height = buildings[i]
    for j in range(i-1, -1, -1):
        if buildings[j] > max_height:
            max_height = buildings[j]
            temp.append(j)

    max_height = buildings[i]
    for j in range(i+1, n+1):
        if buildings[j] > max_height:
            max_height = buildings[j]
            temp.append(j)
    
    ans.append(temp)

for a in ans:
    if a:
        print(f"{len(a)} {a[0]}")
    else:
        print(0)
print(ans)
stack = []
idx_stack = [[] for _ in range(n+1)]
for b in buildings:
    stack.append([b])
print(idx_stack)
print(stack)
for i in range(1, n+1):
    if not stack:
        stack.append(buildings[i])