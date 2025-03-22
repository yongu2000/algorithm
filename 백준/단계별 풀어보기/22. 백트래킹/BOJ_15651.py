def dfs():
    if len(sequences) == m:
        answer.append(" ".join(map(str, sequences)))
        return
        
    for i in range(1, n+1):
        sequences.append(i)
        dfs()
        sequences.pop()

n, m = map(int, input().split())
sequences = []
answer = []

dfs()
print("\n".join(answer))