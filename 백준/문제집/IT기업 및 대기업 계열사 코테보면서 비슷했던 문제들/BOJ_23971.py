import sys
h, w, n, m = map(int, input().split())
answer = ((h // (n+1))+1) * ((w // (m+1))+1)
print(answer)
