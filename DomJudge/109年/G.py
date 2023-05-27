while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        r = n[0]
        n = n[2:]
        z = [0]*(r+1)
        for i in n:
            for u in range(r,i-1,-1):
                z[u] = max(z[u-i]+i,z[u])
        print(max(z))
    except:
        break