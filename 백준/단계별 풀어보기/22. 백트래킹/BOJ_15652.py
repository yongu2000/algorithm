def dfs():
    if len(sequences) == m and set(sequences) not in visited:
        answer.append(" ".join(map(str, sequences)))
        visited.append(set(sequences))
        
    for i in range(1, n+1):
        if i not in sequences:
            sequences.append(i)
            dfs()
            sequences.pop()

n, m = map(int, input().split())
sequences = []
visited = []
answer = []

dfs()
print("\n".join(answer))