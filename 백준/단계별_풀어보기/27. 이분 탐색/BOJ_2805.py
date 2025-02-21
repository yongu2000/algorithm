import sys
input = sys.stdin.readline

def num_of_slice(length):
    result = 0
    for tree in trees:
        if tree >= length:
            result += tree - length
    return result

def search_max_height(trees):
    start = 1
    end = max(trees)

    while start <= end:
        mid = (start + end) // 2
    
        num = num_of_slice(mid)
        if num >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end

n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(search_max_height(trees))
