for _ in range(int(input())):
    a = int(input())
    z = [0]*a
    r = {}
    b = int(input())
    for i in range(b):
        n = [int(_) for _ in input().split(' ') if _]
        if r.get(n[0],"None") == "None":r[n[0]] = [n[1]]
        else:r[n[0]].append(n[1])
        if r.get(n[1],"None") == "None":r[n[1]] = [n[0]]
        else:r[n[1]].append(n[0])
    z[0] = 1
    t = "T"
    for i in range(a):
        for u in r[i]:
            if z[u] == 0:
                if z[i] == 1:z[u] = 2
                else:z[u] = 1
            else:
                if z[i] == z[u]:
                    t = 'F'
                    break
        if t == 'F':break
    print(t)