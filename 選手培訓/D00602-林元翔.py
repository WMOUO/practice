for _ in range(eval(input())):
    d = dict()
    a = []
    z = dict()
    number = -1
    ans = 0
    t = True
    
    for i in [n for n in input().split(" ") if n]:
        i = str(i).split(",")
        if z.get(i[0],"None") == 'None':z[i[0]] = None
        if z.get(i[1],"None") == 'None':z[i[1]] = None
        if d.get(int(i[2]),"None") == "None":
            d[int(i[2])] = [str(i[0])+","+str(i[1])]
        else:
            d[int(i[2])].append(str(i[0])+','+str(i[1]))
    key = sorted(list(d.keys()))
    
    for i in key:
        if t == False:break
        for u in d[i]:
            if t == False:break
            u = u.split(",")
            if z[u[0]] == z[u[1]]:
                if z[u[0]] == None:#兩個都沒練接
                    number += 1
                    a.append(number)
                    z[u[0]] = number
                    z[u[1]] = number
                    ans += i
            else:
                if z[u[0]] == None:
                    z[u[0]] = a[z[u[1]]]
                elif z[u[1]] == None:
                    z[u[1]] = a[z[u[0]]]
                else:
                    if z[u[0]] > z[u[1]]:
                        a[z[u[0]]] = z[u[1]]
                    else:
                        a[z[u[1]]] = z[u[0]]
                ans += i
            n = list(z.values())
            if None not in n:    
                for _ in a:
                    if _ != 0:
                        t = True
                        break
                    else:
                        t =False
    print(ans)