import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    parenthesis = list(input().strip())
    ans = []
    VPS = True
    for p in parenthesis:
        if p == '(':
            ans.append('(')
        elif len(ans) == 0 and p == ')':
            VPS = False
            break
        else:
            ans.pop()
            
    if len(ans) == 0 and VPS:
        print("YES")
    else:
        print("NO")