for _ in range(int(input())):
    z = []
    ans = 0
    for __ in range(int(input())):
        z.append(input())
    for i in z:
        w = 1
        for u in z:
            if i == u:continue
            while i[:w] == u[:w]:
                w += 1
                continue
        ans += w
    print(ans)