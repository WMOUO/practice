for _ in range(int(input())):
    z = []
    ans = ''
    h,b = map(int,input().split(' '))
    for __ in range(h):
        n = input()
        z.append(n)
    for i in range(b):
        a = 0
        c = 0
        g = 0
        t = 0
        ax = 0
        for u in range(h):
            k = z[u]
            if k[i] == 'A':
                a += 1
                if a > ax:ax = a
            elif k[i] == 'C':
                c += 1
                if c > ax:ax = c
            elif k[i] == 'G':
                g += 1
                if g > ax:ax = g
            elif k[i] == 'T':
                t += 1
                if t > ax:ax = t                
        if a == ax:ans += 'A'
        elif c == ax:ans += 'C'
        elif g == ax:ans += 'G'
        else:ans += "T"
    print(ans)