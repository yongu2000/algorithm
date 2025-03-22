def dfs(start):
    if len(sequences) == m:
        answer.append(" ".join(map(str, sequences)))

    for i in range(1, n+1):
        if i not in sequences:
            sequences.append(i)
            dfs(i)
            sequences.pop()

n, m = map(int, input().split())
sequences = []
answer = []

dfs(1)
print("\n".join(answer))