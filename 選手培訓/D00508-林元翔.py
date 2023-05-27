for _ in range(int(input())):
    d = {}
    f = dict()
    x = []
    find = False
    n = [n for n in input().split(" ") if n]
    for i in n:
        i = i.split(",")
        i = list(map(int,i))
        if d.get(i[0],'None') != 'None' :
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
            f[i[0]] = -1
        if d.get(i[1],'None') != 'None' :
            d[i[1]].append(i[0])
        else:
            d[i[1]] = [i[0]]
            f[i[1]] = -1
    z = list(d.keys())
    if len(z)-1 == len(n):
        print("T")
    elif len(z) != len(n):
        print("F")
    else:
        x.append(z[0])
        while find == False:
            b = x[-1]
            a = d[b]
            f[b] += 1
            a = a[f[b]]
            if len(x) >= 2 :
                if a == x[-2] or 1 == len(d[a]):
                    if f[b] == len(d[b])-1:
                        x = x[:-1]
                    continue
            if f[b] == len(d[b]):
                x = x[:-1]
                continue
            else:
                if a in x:
                    for u in range(len(x)):
                        if x[u] == a:
                            p = u
                            find = True
                            break
                else:x.append(a)
        z = x[p:]
        z = sorted(z)
        z = list(map(str,z))
        print(", ".join(z))