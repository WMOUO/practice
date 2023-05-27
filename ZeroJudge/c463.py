z = {}
n = int(input())
w = [int(_) for _ in range(1,n+1)]
p = [0]*(n+1)
k = []
for i in range(1,n+1):
    r = [int(_) for _ in input().split(' ') if _]
    if r[0] != 0:
        for u in r[1:]:
            w[u-1] = 0
            z[u] = i
    else:
        k.append(i)
a = sum(w)
print(a)
l = 0
while True:
    h = set()
    l += 1
    for i in k:
        if i != a:
            p[z[i]] = l
            h.add(z[i])
    if len(h) == 0:
        break
    k = list(h)
print(sum(p))