for _ in range(int(input())):
    a = int(input())
    n = [int(_) for _ in input().split(',') if _]
    c = n.pop(0)
    z = {c:[None,None]}
    ans = []
    for i in n:
        a = c
        z[i] = [None,None]
        while True:
            if i > a:
                if z[a][1] == None:
                    z[a][1] = i
                    break
                else:
                    a = z[a][1]
            else:
                if z[a][0] == None:
                    z[a][0] = i
                    break
                else:
                    a = z[a][0]
    r = [c]
    while True:
        if z[r[-1]][0] != None:
            r.append(z[r[-1]][0])
            if len(r) >= 2:
                z[r[-2]][0] = None
        elif z[r[-1]][1] != None:
            r.append(z[r[-1]][1])
            if len(r) >= 2:
                z[r[-2]][1] = None
        else:
            ans.append(r[-1])
            r.pop(-1)
        if len(r) == 0:
            break
    ans = map(str,ans)
    print(','.join(ans))