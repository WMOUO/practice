for _ in range(int(input())):
    a,b = map(int,input().split(','))
    z = []
    ans = 0
    w = 0
    for _ in range(a):
        n = [int(_)  for _ in input().split(',') if _]
        z.append(n)
        if n[1] == 99:
            r = [n[0]]
    while w < b:
        w += 1
        e = []
        for i in r:
            for u in z:
                if i == u[1]:
                    if w == b:
                        ans += 1
                    else:
                        e.append(u[0])
            r = e
    print(ans)