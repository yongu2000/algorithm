import sys
from functools import reduce
input = sys.stdin.readline

exp = input().strip().split("-")

for i in range(len(exp)):
    exp[i] = sum(list(map(int, exp[i].split("+"))))
print(reduce(lambda x, y : x - y, exp))
