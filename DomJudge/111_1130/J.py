z = [0]+[1,0]*50000
z[1],z[2] = 0,1
r = [2]
for i in range(3,len(z)):
    if z[i] == 1:
        r.append(i)
        for u in range(i*i,len(z),i):
            z[u] = 0
for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    for i in range(n[0],n[1]+1):
        if i < 100001:
            if z[i] == 1:
                print(i)
        else:
            t = True
            for u in r:
                if i % u == 0:
                    t = False
                    break
            if t == True:
                print(i)
    print()