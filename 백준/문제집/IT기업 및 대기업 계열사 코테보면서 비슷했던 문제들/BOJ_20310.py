import sys
input = sys.stdin.readline

S = list(input().strip())

zero = S.count("0") // 2
one = S.count("1") // 2

for s in S:
    if one == 0:
        break
    if s == "1":
        S.remove(s)
        one -= 1

S = S[::-1]
for s in S:
    if zero == 0:
        break
    if s == "0":
        S.remove(s)
        zero -= 1
print("".join(S[::-1]))