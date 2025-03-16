import sys
input = sys.stdin.readline

n, b = map(int, input().split())
ans = []
while n // b > 0:
    value = n // b
    remainder = n % b
    if remainder > 9:
        ans.append(chr(remainder+55))
    else:
        ans.append(str(remainder))
    n = value
if n > 9:
    ans.append(chr(n+55))
else:
    ans.append(str(n))
ans.reverse()
print("".join(ans))
