import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, t, m = map(int, input().split())

    data = [[0]*(k+1) for _ in range(n+1)]

    final_score = {}
    submit_count = {} 
    submit_order = {}

    submit = []
    for _ in range(m):
        i, j, s = map(int, input().split())
        submit.append(i)
        data[i][j] = max(data[i][j], s)
    
    for index, val in enumerate(list(map(sum, data))):
        final_score[index] = val
    del final_score[0]

    for s in set(submit):
        submit_count[s] = submit.count(s)

    for i in range(len(submit)):
        submit_order[submit[i]] = i

    result = sorted([i for i in range(1, n+1)], 
                    key= lambda x: (-final_score[x], submit_count[x], submit_order[x]))
    print(result.index(t)+1)