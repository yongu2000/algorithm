import sys
input = sys.stdin.readline

def fac(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def fac2(n, k):
    res = 1
    for i in range(n, n-k, -1):
        res *= i
    return res

n, k = map(int, input().split())

print(fac2(n, k) // fac(k))