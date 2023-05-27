a = [int(_) for _ in input().split(' ') if _]
z = []
for _ in range(a[0]):
    z.append([int(_) for _ in input().split(' ') if _])
w = [int(_) for _ in input().split(' ') if _][::-1]
for i in w:
    if i == 0:
        h = [[0 for _ in range(len(z))] for _ in range(len(z[0]))]
        for u in range(len(z)):
            for j in range(len(z[u])):
                h[len(z[u])-j-1][u] = z[u][j]
        z = h
    else:
        for u in range(len(z)//2):
            z[u], z[len(z)-u-1] = z[len(z)-u-1], z[u]
print(len(z), len(z[0]))
for i in z:
    i = map(str, i)
    print(' '.join(i))