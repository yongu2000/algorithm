import sys
input = sys.stdin.readline

n = int(input())
channels = [input().strip() for _ in range(n)]
commands = []

kbs1 = "KBS1"
kbs2 = "KBS2"

kbs1_idx = channels.index(kbs1)
kbs2_idx = channels.index(kbs2)

if kbs1_idx > kbs2_idx:
    kbs2_idx += 1

for _ in range(kbs1_idx):
    commands.append(1)
for _ in range(kbs1_idx):
    commands.append(4)

for _ in range(kbs2_idx):
    commands.append(1)
for _ in range(kbs2_idx-1):
    commands.append(4)
print("".join(map(str, commands)))
