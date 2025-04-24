import sys
input = sys.stdin.readline

n = int(input())
shortcuts = set()

for _ in range(n):
    option = list(input().strip().split())
    new_option = []

    shortcut = ""
    for word in option:
        if word[0] not in shortcuts and not shortcut:
            shortcut = word[0]
            shortcuts.update(word[0].upper(), word[0].lower())
            temp = list(word)
            temp[0] = f"[{word[0]}]"
            word = "".join(temp)
        
        new_option.append(word)


    if not shortcut:
        new_option = []
        for word in option:
            for i, w in enumerate(word):
                if w not in shortcuts and not shortcut:
                    shortcut = w
                    shortcuts.update(w.upper(), w.lower())

                    temp = list(word)
                    temp[i] = f"[{w}]"
                    word = "".join(temp)
            new_option.append(word)    

    ans = " ".join(new_option)
    print(ans)