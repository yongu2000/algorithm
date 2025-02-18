import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())
sums = [[0] * (len(S)+1) for _ in range(26)]

for i in range(26):
    count = 0
    for j in range(1, len(S)+1):
        if S[j-1] is chr(i + 97):
            count += 1
            sums[i][j] = count
        else:
            sums[i][j] = count

for _ in range(q):
    a, n, m = input().split()
    n = int(n) + 1
    m = int(m) + 1
    print(sums[ord(a) - 97][m] - sums[ord(a) - 97][n-1])