while True:
    a = int(input())
    if a == 0:
        break
    while True:
        n = [int(_) for _ in input().split(' ') if _]
        t = True
        if len(n) == 1 and n[0] == 0:
            break
        r = n[0]
        p = r
        for i in n[1:]:
            if r < i:
                if i < p:
                    t = False
                    break
            p = max(p,i)
            r = i
        if t == False:
            print("No")
        else:
            print("Yes")