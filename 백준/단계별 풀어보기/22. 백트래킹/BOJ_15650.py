def dfs(start):
    if len(sequences) == m:
        answer.append(" ".join(map(str, sequences)))
        return

    for i in range(start, n+1):
        sequences.append(i)
        dfs(i)
        sequences.pop()

n, m = map(int, input().split())
sequences = []
answer = []

dfs(1)
print("\n".join(answer))