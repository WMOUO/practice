a,b = [int(_) for _ in input().split(' ') if _]
z = []
for _ in range(a):
    r = [int(_) for _ in input().split(' ') if _]
    z[(r[0]*2)**2*r[2]] = [r[0],r[1]]
# z.sort(key=lambda z:(z[0],-z[1]))
u = z.keys()
u.sort()
u = u[:b]
t,y = 0,0
for i in u:
    t = max(t,z[u[0]])
    y = max(y,z[u[1]])
print((t*2)**2*y) 