n = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))

mx = -1000000001
mn = 1000000001

def solve(i, result):
    global mx, mn
    if i == n-1:
        mx = max(mx, result)
        mn = min(mn, result)
        return 
    
    if operations[0] != 0:
        operations[0] -= 1
        solve(i+1, result+nums[i+1])
        operations[0] += 1

    if operations[1] != 0:
        operations[1] -= 1
        solve(i+1, result-nums[i+1])
        operations[1] += 1

    if operations[2] != 0:
        operations[2] -= 1
        solve(i+1, result*nums[i+1])
        operations[2] += 1

    if operations[3] != 0:
        operations[3] -= 1
        solve(i+1, int(result/nums[i+1]))
        operations[3] += 1
        
solve(0, nums[0])
print(mx)
print(mn)



