import re
from itertools import permutations

def solution(expression):
    tokens = re.split("([-+*])", expression)
    operators = ['+', '-', '*']
    answer = 0

    for p in permutations(operators):
        temp_tokens = tokens[:]
        for op in p:
            stack = []
            i = 0
            while i < len(temp_tokens):
                if temp_tokens[i] == op:
                    left = stack.pop()
                    right = temp_tokens[i+1]
                    res = str(eval(left + op + right))
                    stack.append(res)
                    i += 2 
                else:
                    stack.append(temp_tokens[i])
                    i += 1
            temp_tokens = stack
        answer = max(answer, abs(int(temp_tokens[0])))

    return answer