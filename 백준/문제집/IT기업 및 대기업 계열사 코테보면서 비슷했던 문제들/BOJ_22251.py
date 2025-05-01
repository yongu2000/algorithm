import sys
input = sys.stdin.readline

data = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1], 
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]

def possible(target, current, p):
    for i in range(len(target)):
        p -= data[int(current[i])][int(target[i])]
        if p < 0:
            return False
    return True

n, k, p, x = map(int, input().split())
answer = 0
current = ""

if len(str(x)) < k:
    current = "0"*(k-len(str(x))) + str(x)
else:
    current = str(x)

for i in range(1, n+1):
    if i == x:
        continue
    target = ""
    if len(str(i)) < k:
        target = "0"*(k-len(str(i))) + str(i)
    else:
        target = str(i)
    
    if possible(target, current, p):
        answer += 1
print(answer)