import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))

neutral = sys.maxsize
answer = []

left, right = 0, n-1

while left < right:
    mixture = abs(liquids[left] + liquids[right])

    if mixture == 0:
        answer = [liquids[left], liquids[right]]
        break
        
    if mixture < neutral:
        neutral = mixture
        answer = [liquids[left], liquids[right]]

    if liquids[left] + liquids[right] < 0:
        left += 1
    else:
        right -= 1

print(*answer)