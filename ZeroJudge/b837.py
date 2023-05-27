from bisect import bisect_left
z = [0,1,1]+[0]*29
for i in range(3,32):
    z[i] = z[i-1]+z[i-2]
p = int(input())
for j in range(p):
    n = [int(_) for _ in input().split(' ') if _]
    n[0],n[1] = min(n),max(n)
    a = bisect_left(z,n[0],lo = 0,hi = len(z))
    r = 0
    while True:
        if z[a] <= n[1]:
            print(z[a])
            r += 1
            a += 1
        else:
            break
    print(r)
    if j != p-1:
        print('------')