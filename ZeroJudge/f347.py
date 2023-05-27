z = []
while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        z.append([n[0],n[1]])
    except:
        break
z.sort(key = lambda x:(x[1],x[0]))
w = []
u = [0,0]
r = 0
for i in z:
    r += i[0]
    if i[1] - r < 0:
        if i[0] > u[0]:
            r -= i[0]
            continue
        else:
            w.remove(u)
            r -= u[0]
            w.append(i)
            u = [0,0]
            for j in w:
                if j[0] > u[0]:
                    u = j
    else:
        w.append(i)
        if i[0] > u[0]:
            u = i
print(len(w))