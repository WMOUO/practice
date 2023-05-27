while True:
    try:
        a = [int(_) for _ in input().split() if _]
        for _ in range(a[0]):
            n = [int(_) for _ in input().split() if _]
            n.sort(reverse = True)
            r = sum(n) // 2
            z = [0]*(r+1)
            for i in range(1,len(z)):
                for u in range(len(n)):
                    if n[u] > i:
                        z[u] = max(z[u],z[u-i]+i)
                    else:
                        break
            if z[-1] == r:
                print("Yes")
            else:
                print("No")
    except:
        break