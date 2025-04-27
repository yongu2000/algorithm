import sys
from collections import defaultdict

input = sys.stdin.readline


def find_possible_alphabet(string, k):
    data = defaultdict(int)
    for s in string:
        data[s] += 1

    return list(filter(lambda x : data[x] >= k, data.keys()))

def find_ans(possible_alphabet, string, k):
    data = defaultdict(int)

    left, right = 0, 0

    data[string[left]] += 1

    shortest = 100001
    longest = -1
    for a in possible_alphabet:
        while left != len(string)-1:
            if right < len(string)-1:
                right += 1
                data[string[right]] += 1
            else:
                data[string[left]] -= 1
                left += 1

            if data[string[right]] == k and string[right] == a:
                shortest = min(shortest, right-left)
                longest = max(longest, right-left)
            
            elif data[string[right]] > k and string[right] == a:
                while string[left] == a:
                    data[string[left]] -= 1
                    left += 1        

    return shortest, longest


t = int(input())

for _ in range(t):
    w = input().strip()
    k = int(input())

    possible_alphabet = find_possible_alphabet(w, k)
    if possible_alphabet:
        print(find_ans(possible_alphabet, w, k))
    else:
        print(-1)