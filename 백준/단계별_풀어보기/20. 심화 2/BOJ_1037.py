import sys
input = sys.stdin.readline

n = int(input())
factors = list(map(int, input().split()))

print(min(factors)*max(factors))