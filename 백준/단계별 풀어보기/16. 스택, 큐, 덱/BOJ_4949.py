import sys, re
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == ".":
        break
    
    ans = []
    VPS = True
    parenthesis = list(re.sub("[^\[\]\(\)]", "", string.strip()))

    for p in parenthesis:
        if p == '(' or p == '[':
            ans.append(p)
        elif len(ans) == 0 and (p == ')' or p == ']'):
            VPS = False
            break
        elif p == ')' and ans[len(ans) - 1] == '[':
            VPS = False
            break
        elif p == ']' and ans[len(ans) - 1] == '(':
            VPS = False
            break
        else:
            ans.pop()
            
    if len(ans) == 0 and VPS:
        print("yes")
    else:
        print("no")