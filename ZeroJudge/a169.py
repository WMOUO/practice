z = [int(_) for _ in input().split(" ") if _]
x = []
ans = []
for _ in range(z[0]):
    n = [int(_) for _ in input().split(" ") if _]
    x.append(n)
for _ in range(z[2]):
    p = 0
    m = [int(_) for _ in input().split(" ") if _]
    r,t = m[0],True
    for i in m:
        if i == r:continue
        else:
            t = False
            break
    if t != True:
        for j in range(len(m)):
            i =x[j]
            for u in range(len(i)):
                if m[j] == u:
                    p += i[u]
                else:
                    if i[u] > 1000:
                        p += (3000+(i[u]-1000)*2)
                    else:p += i[u]*3
    else:
        u = [0]*len(n)
        for i in x:
            for j in range(len(i)):
                u[j] += i[j]
        for j in range(len(u)):
            if m[0] == j:p += u[j]
            else:
                if u[j] > 1000:
                    p += (3000+(u[j]-1000)*2)
                else:p += u[j]*3
    ans.append(p)
print(min(ans))