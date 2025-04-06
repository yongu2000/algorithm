import sys
input = sys.stdin.readline

n, game = input().strip().split()
n = int(n)

ans = 0
played = set()
temp = set()
for _ in range(n):
    player = input().strip()
    
    if game == "Y" and player not in temp and player not in played:
        temp.add(player)
        if len(temp) == 1:
            played.update(temp)
            ans += 1
            temp = set()
    elif game == "F" and player not in temp and player not in played:
        temp.add(player)
        if len(temp) == 2:
            played.update(temp)
            ans += 1
            temp = set()
    elif game == "O" and player not in temp and player not in played:
        temp.add(player)
        if len(temp) == 3:
            played.update(temp)
            ans += 1
            temp = set()

print(ans)