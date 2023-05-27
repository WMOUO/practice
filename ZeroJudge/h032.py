z = {}
a = int(input())
r = 0
real_ans = 0
t = []
for _ in range(a-1):
    n = [int(_) for _ in input().split(' ') if _]
    r = max(r, max(n))
    if max(n)+1 > len(t):
        t += [0]*(max(n)+1-len(t))
    t[n[1]] = 1
    if z.get(n[0], None) == None:
        z[n[0]] = [n[1]]
    else:
        z[n[0]].append(n[1])
w = [t.index(0)]
h = [0]+[0]*r
ans = [[0]]+[[0]]*r
while len(w) != 0:
    p = w[-1]
    if z.get(p, None) != None and len(z[p]) > h[p]:
        w.append(z[p][h[p]])
        h[p] += 1
    else:
        if z.get(p, None) == None:
            ans[p] = [0, 1]
        else:
            if len(z[p]) == 1:
                ans[p] = [ans[z[p][0]][1], ans[z[p][0]][1]+1]
            elif len(z[p]) == 2:
                ans[p] = [ans[z[p][0]][1]+ans[z[p][1]][1],
                          max(ans[z[p][0]][1], ans[z[p][1]][1])+1]
            else:
                k = []
                for i in z[p]:
                    k.append(ans[i])
                k.sort(key=lambda x: -x[1])
                ans[p] = [k[0][1]+k[1][1], k[0][1]+1]
        real_ans = max(real_ans, max(ans[p]))
        w.pop()
print(real_ans)