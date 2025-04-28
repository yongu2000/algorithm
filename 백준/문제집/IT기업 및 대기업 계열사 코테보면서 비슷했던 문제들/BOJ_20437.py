import sys
from collections import defaultdict

input = sys.stdin.readline


def find_possible_alphabet(string, k):
    data = defaultdict(list)

    for i in range(len(string)):
        if string.count(string[i]) >= k: 
            data[string[i]].append(i)
    return data

def find_ans(possible_alphabet, k):
    shortest = 100001
    longest = -1

    for a in possible_alphabet:
        for i in range(len(possible_alphabet[a])-k+1):
            length=possible_alphabet[a][i+k-1]-possible_alphabet[a][i] 

            shortest = min(shortest, length)
            longest = max(longest, length)
    return shortest+1, longest+1


t = int(input())

for _ in range(t):
    w = input().strip()
    k = int(input())

    possible_alphabet = find_possible_alphabet(w, k)
    if possible_alphabet:
        shortest, longest = find_ans(possible_alphabet, k)
        print(shortest, longest)
    else:
        print(-1)