import sys
input = sys.stdin.readline


streak = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
          {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
          {0, 4, 8}, {2, 4, 6}
            ]

def is_end(game):
    X = set()
    O = set()
    for i, g in enumerate(game):
        if g == "X":
            X.add(i)
        elif g == "O":
            O.add(i)
    X_streak = 0
    O_streak = 0
    for s in streak:
        if not s - X:
            X_streak += 1
        if not s - O:
            O_streak += 1

    if X_streak == 2 and O_streak == 0 and len(X) == 5 and len(O) == 4:
        return True
    if X_streak == 1 and O_streak == 0 and len(X) - len(O) == 1:
        return True
    if O_streak == 1 and X_streak == 0 and len(X) == len(O):
        return True
    if X_streak == 0 and O_streak == 0 and len(X) == 5 and len(O) == 4:
        return True
    return False
    
while True:
    game = input().strip()

    answer = "invalid"
    if game == "end":
        break
    
    if is_end(game):
        answer = "valid"
    
    print(answer)