for _ in range(int(input())):
    n = [_ for _ in input().split(' ') if _]
    r = [0]*len(n)
    ans = 0
    for i in range(len(n)):
        if n[i] == 'X':r[i] = 10
        elif n[i] == '/':r[i] = 10-int(n[i-1])
        else:r[i] = int(n[i])
    rank = 1
    level = 0
    i = -1
    while rank < 10:
        i += 1
        if n[i] == "X":
            ans += 10+r[i+1]+r[i+2]
            rank += 1
            level = 0
            continue
        elif n[i] == "/":ans += r[i]+r[i+1]
        else:ans += r[i]
        level += 1
        if level == 2:
            level = 0
            rank += 1
    for u in range(i+1,len(n)):
        if n[u] == 'X' or n[u] == "/":
            ans += sum(r[u:])
            break
        else:ans += r[u]
    print(ans)