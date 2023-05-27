for _ in range(int(input())):
    a,b,c = map(int,input().split(','))
    z = []
    for _ in range(a):
        n = [int(_) for _ in input().split(' ') if _]
        if n[1] == 999:
            a = n[0]
        z.append(n)
    ans = []
    for i in range(1,b+1):
        r = z[c][i]
        p = 1
        while r != a:
            p += 1
            r = z[r][i]
        ans.append(p)
    ans = map(str,ans)
    print(','.join(ans))