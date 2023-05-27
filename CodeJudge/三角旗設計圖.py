z = [int(_) for _ in input().split(' ') if _]
n = []
for i in z:
    if i != 0:
        n.append(i)
r = n.copy()
for u in range(max(n)):
    for i in range(len(r)):
        if r[i] == 0:
            print(' '*((n[i]-1)*2+1),end = ' ')
        elif i == len(r)-1:
            print(' '*(n[i]-r[i])+'*'*((r[i]-1)*2+1))
        else:
            print(' '*(n[i]-r[i])+'*'*((r[i]-1)*2+1)+' '*(n[i]-r[i]),end = ' ')
        r[i] = max(0,r[i]-1)
    while len(r) > 0 and r[-1] == 0:
        r.pop()