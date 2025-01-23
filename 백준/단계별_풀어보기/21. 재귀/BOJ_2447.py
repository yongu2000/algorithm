def star(n):
    if n == 1:
        return "*"
    stars = star(n//3)
    answer = []
    for s in stars:
        answer.append(s * 3)
    for s in stars:
        answer.append(s + " " * (n//3) + s)
    for s in stars:
        answer.append(s * 3)
    return answer

print("\n".join(star(int(input()))))
