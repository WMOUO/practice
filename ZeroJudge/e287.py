a = [int(_) for _ in input().split(' ') if _]
z = [[-1]*(a[1]+1)]
r = [0,0]
h = float('inf')
for i in range(a[0]):
    n = [int(_) for _ in input().split(' ') if _]
    z.append([-1]+n+[-1])
    if h > min(n):
        h = min(n)
        r = [i+1,n.index(h)+1]
z.append([-1]*(a[1]+1))
ans = z[r[0]][r[1]]
while True:
    h = float('inf')
    t = 0
    if z[r[0]-1][r[1]] != -1 and z[r[0]-1][r[1]] < h:
        h = z[r[0]-1][r[1]]
        t = 1
    if z[r[0]+1][r[1]] != -1 and z[r[0]+1][r[1]] < h:
        h = z[r[0]+1][r[1]]
        t = 2
    if z[r[0]][r[1]-1] != -1 and z[r[0]][r[1]-1] < h:
        h = z[r[0]][r[1]-1]
        t = 3
    if z[r[0]][r[1]+1] != -1 and z[r[0]][r[1]+1] < h:
        h = z[r[0]][r[1]+1]
        t = 6
    if t != 0:
        z[r[0]][r[1]] = -1
        if t == 1:
            r[0] -= 1
        elif t == 2:
            r[0] += 1
        elif t == 3:
            r[1] -= 1
        elif t == 6:
            r[1] += 1
        ans += h
    else:
        break
print(ans)