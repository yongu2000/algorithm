import sys
input = sys.stdin.readline

n, m = map(int, input().split())

title = []
powers = []
for _ in range(n):
    name, value = map(str, input().split())
    if powers and powers[-1] == value:
        continue
    title.append(name)
    powers.append(int(value))

for _ in range(m):
    power = int(input())
    
    left = 0
    right = len(powers)-1

    while left <= right:
        mid = (left + right) // 2
        if powers[mid] < power:
            left = mid + 1
        else:
            right = mid - 1
    print(title[left])