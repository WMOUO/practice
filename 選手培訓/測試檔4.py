#701
for _ in range(eval(input())):
    d = dict()
    go = dict()
    z = []
    all = 0
    ans = 0
    for i in [n for n in input().split(" ") if n]:
        i = str(i).split(",")
        if i[0] not in z:z.append(i[0])
        if i[1] not in z:z.append(i[1])
        if d.get(int(i[2]),"None") == "None":
            d[int(i[2])] = [str(i[0])+","+str(i[1])]
        else:
            d[int(i[2])].append(str(i[0])+','+str(i[1]))    
    for i in z:
        go[i] = str(-1)
    z = len(z)-1
    key = sorted(list(d.keys()))
    for i in key:
        if all == z:break
        for u in d[i]:
            if all == z :break
            u = str(u).split(",")
            if go[u[1]] == go[u[0]] and go[u[1]] != "-1" or go[u[0]] != "-1" and go[u[1]] != "-1":
                continue
            else:
                go[u[1]] = u[0]
                ans += i
                all += 1
    print(ans)