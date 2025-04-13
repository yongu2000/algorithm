import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(input().strip())

def eat_hamburger(x):
    left = max(0, x-k)
    right = min(n-1, x+k)
    
    for i in range(left, right+1):
        if data[i] == "H":
            data[i] = "E"
            break


for i in range(n):
    if data[i] == "P":
        eat_hamburger(i)
print(data.count("E"))
    