a = [int(_) for _ in input().split(' ') if _]
z = {}
r = [0]*(a[0]+1)
for i in range(a[1]):
    n = [int(_) for _ in input().split(' ') if _]
    if z.get(n[0],None) == None:
        z[n[0]] = [n[1]]
    else:
        z[n[0]].append(n[1])
for _ in range(a[2]):
    w = [int(input())]
    r[w[0]] = 1
    while True:
        h = set()
        for i in w:
            if z.get(i,None) != None:
                for u in z[i]:
                    if r[u] != 1:
                        h.add(u)
                        r[u] = 1
        if len(h) == 0:
            break
        w = list(h)
for _ in range(a[3]):
    if r[int(input())] == 0:
        print('YA~~')
    else:
        print('TUIHUOOOOOO')