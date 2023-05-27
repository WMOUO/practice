n = [int(_) for _ in input().split(' ') if _]
z = []
a = len(n)//3
b = 0
c = a
for i in range(3):
    z.append(n[b:c])
    b += a
    c += a
ans = []
for i in range(a):
    b = 0
    c = 0
    for u in z:
        if u[i] > b:
            c,b = b,u[i]
        elif u[i] > c:
            c = u[i]
    ans.append(c)
print([ans]*3)