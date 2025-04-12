import sys, math
input = sys.stdin.readline

switch = int(input())
switches = list(map(int, input().split()))
switches.insert(0, 0)
student = int(input())

for _ in range(student):
    gender, number = map(int, input().split())
    i = 1
    if gender == 1:
        while number*i <= switch:
            switches[number*i] = 1-switches[number*i] 
            i += 1
    elif gender == 2:

        switches[number] = 1 - switches[number]
        while 0 < number+i <= switch and 0 < number-i <= switch and switches[number+i] == switches[number-i]:
            switches[number+i] = 1 - switches[number+i]
            switches[number-i] = 1 - switches[number-i]
            i += 1

index = int(math.ceil(switch / 20))
for i in range(index):
    count = 20 * i
    if i != index - 1:
        print(*switches[count+1:count+21])
    else:
        print(*switches[count+1:])
