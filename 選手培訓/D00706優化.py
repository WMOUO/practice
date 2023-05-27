while True:
    try:
        n,m = map(int,input().split(" "))
        r = [0]
        w = [ int(_) for _ in input().split(" ") if _ ]
        v = [ int(_) for _ in input().split(" ") if _ ]
        w = r+w
        v = r+v
        z = [0]*(m+1)
        for i in range(1,n+1): #號碼
            for u in range(m,0,-1): #重
                if u >= w[i]:
                    z[u] = max(z[u],z[u-w[i]]+v[i])
        print(max(z))
    except:
        break