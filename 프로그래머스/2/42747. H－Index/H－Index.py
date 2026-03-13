from bisect import bisect_left

def solution(citations):
    answer = 0
    citations.sort()
    
    left = 0
    right = len(citations)
    
    while left <= right:
        mid = (left + right) // 2
        
        count = len(citations) - bisect_left(citations, mid)
        if mid <= count:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
        
    return answer