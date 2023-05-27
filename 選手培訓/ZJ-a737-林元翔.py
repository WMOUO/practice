for _ in range(int(input())):
    n  = [int(n) for n in input().split(" ") if n]
    n = n[1:]
    n.sort()
    if len(n) <= 1:
        print(0)
        continue
    ans = 0
    w = []
    c = len(n) // 2
    if len(n) %2 == 0:
        d = (n[c-1]+n[c]) // 2
        for i in n:
            ans += abs(i-d)
        w.append(ans)
        if len(n) >= 3:
            ans = 0
            d = (n[c+1]+n[c]) // 2
            for i in n:
                ans += abs(i-d)
            w.append(ans)
        print(min(w))
    else:
        ans = 0
        for i in n:
            ans += abs(i-n[c])
        print(ans)
    #a = (max(n) + min(n)) / 2
    #6 8 4 5 1 3 2 2 3 3 3 3 3 3