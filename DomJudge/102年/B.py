for _ in range(int(input())):
    z = {}
    for _ in range(int(input())):
        n = input().replace(',',' ')
        n = [_ for _ in n.split(' ') if _]
        for i in n:
            if z.get(i,None) == None:
                z[i] = 1
            else:
                z[i] += 1
    r = z.items()
    w = 0
    for i in r:
        if i[1] > w:
            ans = str(i[0])+', '
            w = i[1]
        elif i[1] == w:
            ans += str(i[0])+', '
    print(ans[:-2])