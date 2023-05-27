for _ in range(int(input())):
    n = input().strip()
    n = n[1:-1]
    n = n.replace(',',' ')
    n = [_ for _ in n.split(' ') if _]
    w = 0
    i = 0
    while True:
        if len(n) < 2**i:
            break
        w += 2**i
        i += 1
    n = n + ['null'] * (w - len(n))
    z = [[0,1] for _ in range(len(n))]
    for u in range(len(n)):
        if n[u] == "null":
            z[u][1] = 0
    i -= 1
    while True:
        w -= 2 ** i
        if w == 0:break
        i -= 1
        a = w - 2**i
        for u in range(2**i):
            z[a][0] = max(z[w][1]+z[w+1][1] , z[w][0]  ,z[w+1][0])
            if z[w][1] != 0 or z[w+1][1] != 0:
                z[a][1] = max(z[w][1] , z[w+1][1])+1
            a += 1
            w += 2
        a -= u+1
        w -= (u+1)*2
    print(z[0][0])

#[6,null,7]
#[1,2,99,null,null,3]
#[1,2,3,4,6,null,7]
#[1,1,1,null,null,1,1,null,null,null,null,1,1,1,1,null,null,null,null,null,null,null,null,1,1,null,null,null,null,1,1,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1,1]