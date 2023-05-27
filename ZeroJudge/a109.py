for _ in range(int(input())):
    n = input()
    t = len(n)
    u = 0
    a = n[0]
    b = 0
    z = []
    r = True
    for i in n:
        if i != '0' and i != '1':
            r = False
            break
        if a == i and b < 7:b += 1
        else :
            c = bin(b)
            c = c[2:]
            if len(c) == 1:c = '00'+c
            elif len(c) == 2: c = '0'+c
            z.append(a+c)
            u += len(a+c)
            a = i
            b = 1
    if r == True:
        c = bin(b)
        c = c[2:]
        if len(c) == 1:c = '00'+c
        elif len(c) == 2: c = '0'+c
        z.append(a+c)
        u += len(a+c)
        a = i
        b = 1
        y = int((u / t)*100)
        z.append(str(y)+'%')
        print(' '.join(z))
    else:print(-1)