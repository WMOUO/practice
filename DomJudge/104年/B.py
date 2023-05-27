import copy
a = int(input())
n = [int(_) for _ in input().split(',') if _]
for _ in range(a):
    z = [0,0,0,0]
    r = [int(_) for _ in input().split(',') if _]
    for i in range(6):
        w = r.copy()
        w.pop(i)
        p = 0
        for u in w:
            if u in n:
                p += 1
        if p >= 2 :
            z[p-2] += 1
    z = map(str,z)
    print(','.join(z))