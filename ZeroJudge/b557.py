from collections import Counter
z = {}
for i in range(1,101):
    for o in range(i,101):
        for u in range(o,101):
            if i**2 + o**2 == u**2:
                if z.get(i,None) == None:
                    z[i] = [(o,u)]
                else:
                    z[i].append((o,u))
for _ in range(int(input())):
    a = input()
    n = [int(_) for _ in input().split(' ') if _]
    r = Counter(n)
    ans = 0
    for i in r.keys():
        if z.get(i,None) != None:
            for u in z[i]:
                if u[0] in n and u[1] in n:
                    ans += r[i]*r[u[0]]*r[u[1]]
    print(ans)