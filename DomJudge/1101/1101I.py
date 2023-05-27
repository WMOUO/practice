while True:
    try:
        a,b,c,d = map(int,input().split(' '))
        z = []
        r = []
        ans = [[0]*d for _ in range(a)]
        for _ in range(a):
            n = [int(_) for _ in input().split(' ') if _]
            z.append(n)
        for _ in range(c):
            n = [int(_) for _ in input().split(" ") if _]
            r.append(n)
        for i in range(a):
            for u in range(d):
                for k  in range(len(z[i])):
                    ans[i][u] += z[i][k]*r[k][u]
                ans[i][u] = str(ans[i][u])
        for _ in ans:
            print(' ' .join(_))
    except:
        break