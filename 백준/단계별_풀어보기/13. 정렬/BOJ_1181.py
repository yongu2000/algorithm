n = int(input())
words = list()
for _ in range(n):
    words.append(input())
words = list(set(words))
words.sort(key = lambda x : (len(x), x))
print("\n".join(words))