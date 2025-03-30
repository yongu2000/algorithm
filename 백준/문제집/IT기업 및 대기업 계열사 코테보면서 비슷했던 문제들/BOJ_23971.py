import sys
h, w, n, m = map(int, input().split())
answer = ((h+n) // (n+1)) * ((w+m) // (m+1))
print(answer)
