import sys
input = sys.stdin.readline


def equation(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)

    b = y1 - slope*x1

    for index in range(x1+1, x2):
        if slope * index + b <= buildings[index]:
            return False
    return True


n = int(input())
buildings = list(map(int, input().split()))

max_val = -1
for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        if i < j and equation(i, buildings[i], j, buildings[j]):
            count += 1
        elif j < i and equation(j, buildings[j], i, buildings[i]):
            count += 1
    
    max_val = max(max_val, count)

print(max_val)