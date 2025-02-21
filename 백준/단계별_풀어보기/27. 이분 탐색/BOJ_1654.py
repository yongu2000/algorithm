import sys
input = sys.stdin.readline

def num_of_slice(length):
    result = 0
    for line in lines:
        result += line // length
    return result

def search_min_len(lines):
    start = 1
    end = max(lines)

    while start <= end:
        mid = (start + end) // 2
    
        if num_of_slice(mid) >= n:
            start = mid + 1
        elif num_of_slice(mid) < n:
            end = mid - 1
    return end

k, n = map(int, input().split())
lines = list(int(input()) for _ in range(k))

print(search_min_len(lines))
