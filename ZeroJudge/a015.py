a = [int(_) for _ in input().split(' ') if _]
z = [[0]*a[0] for _ in range(a[1])]
for _ in range(a[0]):
    b = 0
    n = [int(_) for _ in input().split(' ') if _]
    for i in n:
        z[b][_] = i
        b += 1
for i in z:
    i = list(map(str,i))
    print(' '.join(i))