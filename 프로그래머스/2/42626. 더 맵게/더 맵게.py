import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville and scoville[0] < K:
        if len(scoville) < 2:
            return -1
        t1 = heapq.heappop(scoville)
        t2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville, t1 + t2*2)
        answer += 1
    
    return answer