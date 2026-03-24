answer = 0

def dfs(idx, num, numbers, target):
    global answer
    if idx == len(numbers) and num == target:
        answer += 1
    
    if idx < len(numbers):
        dfs(idx+1, num + numbers[idx], numbers, target)
        dfs(idx+1, num - numbers[idx], numbers, target)
    return
   
def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer