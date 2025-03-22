import sys
input = sys.stdin.readline
n = int(input())
ans = 0
row = [0]*n

def possible(q):
    for i in range(q):
        if row[q] == row[i] or abs(row[q] - row[i]) == abs(q - i):
            return False
    return True

def n_queen(q):
    global ans
    if q == n:
        ans += 1
        return

    for i in range(n):
        row[q] = i
        if possible(q):
            n_queen(q+1)

n_queen(0)
print(ans)
