import sys
input = sys.stdin.readline


def x_to_left(x, data):
    count = 0
    prev = data[0]
    for i in range(1, n):
        if data[i] == x and prev != x:
            count += 1
            prev = ""
        else:
            prev = data[i]
    return count

def red_to_left():
    return x_to_left("R", balls)

def red_to_right():
    return x_to_left("R", list(reversed(balls)))

def blue_to_left():
    return x_to_left("B", balls)

def blue_to_right():
    return x_to_left("B", list(reversed(balls)))


n = int(input())
balls = input().strip()

print(min(red_to_left(), red_to_right(), blue_to_left(), blue_to_right()))