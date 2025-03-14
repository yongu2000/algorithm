import sys
input = sys.stdin.readline

def counts():
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

n, m = map(int, input().split())

words = [input().strip() for _ in range(n)]
words = list(filter(lambda word: len(word) >= m, words))

counts = counts()

words.sort(key = lambda x : (-counts[x], -len(x), x))
ans = list(dict.fromkeys(words))
for a in ans:
    print(a)