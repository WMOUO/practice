while True:
    try:
        a, b, c = map(int, input().split(' '))
        z = []
        for _ in range(a):
            z.append([int(_) for _ in input().split(' ') if _])
        n = [int(_) for _ in input().split(' ') if _]
        n.reverse()
        for i in n:
            if i == 1:
                for u in range(len(z)//2):
                    z[u], z[len(z)-1-u] = z[len(z)-1-u], z[u]
            else:
                r = []
                for u in range(len(z)):
                    for j in range(len(z[u])):
                        if u == 0:
                            r.append([z[u][len(z[u])-1-j]])
                        else:
                            r[j].append(z[u][len(z[u])-1-j])
                z = r
        print(f'{len(z)} {len(z[0])}')
        for i in z:
            i = map(str, i)
            print(' '.join(i))
    except:
        break