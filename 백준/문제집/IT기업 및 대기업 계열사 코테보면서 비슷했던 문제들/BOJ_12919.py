import sys
input = sys.stdin.readline

def dfs(string):

    if len(string) == len(s):
        if string == s:
            print(1)
            exit()
        return  
    
    if string[-1] == "A":
        dfs(string[:-1])
    if string[0] == "B":
        dfs(string[1:][::-1])

    return 0

s = input().strip()
t = input().strip()

print(dfs(t))