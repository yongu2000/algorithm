import sys
input = sys.stdin.readline

word = input().strip().lower()
word_count = dict()

for w in word:
    if w not in word_count: 
        word_count[w] = 1
    else:
        word_count[w] += 1

max_num = -1
ans = []

for val in word_count.values():
    if max_num < val:
        max_num = val

for key, val in word_count.items():
    if max_num == val:
        ans.append(key)
if len(ans) >= 2 or not ans:
    print("?")
else:
    print(ans[0].upper())
