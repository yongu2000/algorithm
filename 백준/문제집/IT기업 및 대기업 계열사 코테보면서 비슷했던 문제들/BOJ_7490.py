import sys
input = sys.stdin.readline

def calculate(string):
    if eval(string.replace(" ", "")) == 0:
        return True
    return False

def formula(string, n, count):

    if count == n:
        if calculate(string + str(count)):
            answer.append(string + str(count))
        return

    steps = [" ", "+", "-"]
    for s in steps:
        formula(string + str(count) + s, n, count+1)

t = int(input())

for _ in range(t):
    n = int(input())
    answer = []
    
    formula("", n, 1)
    print("\n".join(answer))
    print()
