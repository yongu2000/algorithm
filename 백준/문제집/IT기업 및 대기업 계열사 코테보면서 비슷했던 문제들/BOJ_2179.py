import sys
input = sys.stdin.readline

def prefix_eq(string1, string2):
    count = 0
    for i in range(min(len(string1), len(string2))):
        if string1[i] == string2[i]:
            count += 1
        else:
            break
    return count


n = int(input())

words = [(i, input().strip()) for i in range(n)]
words.sort(key = lambda x : x[1]) 

prefix_data = [0] * n

max_prefix = -1
for i in range(n-1):
    prefix_count = prefix_eq(words[i][1], words[i+1][1])
    prefix_data[words[i][0]] = max(prefix_data[words[i][0]], prefix_count)
    prefix_data[words[i+1][0]] = max(prefix_data[words[i+1][0]], prefix_count)
    max_prefix = max(max_prefix, prefix_count)

answer = []

for i in range(n):
    if prefix_data[words[i][0]] == max_prefix:
        answer.append(words[i])
answer.sort()

ans1 = answer[0][1]
print(ans1)
for i in range(1, len(answer)):
    if prefix_eq(ans1, answer[i][1]) == max_prefix:
        print(answer[i][1])
        break
    
