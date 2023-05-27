while True:
    try:
        z = []
        x = []
        ans = ""
        h = True
        c = None
        for _ in range(int(input())):
            n = [int(n) for n in input().split(" ") if n]
            z.append((n[0],n[1]))
        z.sort()
        start = z[0]
        end = z[-1]
        for _ in range(2):
            x.append(z[0])
            z = z[1:]
        while x[-1] != start or h != False:
            a = x[-2]
            b = x[-1]
            c = z[0]
            d = (a[0]-c[0],a[1]-c[1])
            e = (b[0]-c[0],b[1]-c[1])
            f = d[0]*e[1]-e[0]*d[1]
            if f < 0: # 順時鐘
                z.append(x[-1])
                x = x[:-1]
            else:  # 逆時鐘
                x.append(c)
                z = z[1:]
            if c == end:
                h = False
                z.sort()
                z = z[::-1]
                z.append(start)
        for i in x:
            ans += i
        print(ans)
    except:
        break
#5   8   10
#1 3 1 3 1 3
#2 0 2 0 2 0
#4 2 4 2 4 2
#5 1 5 1 5 1
#3 5 3 5 3 5
#    3 2 3 2
#    2 2 2 2
#    3 3 3 3
#        5 3
#        5 4