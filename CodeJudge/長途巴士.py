a,b = map(int,input().split(' '))
r = [0]*999
for _ in range(b):
    n = [int(_) for _ in input().split(' ') if _]
    for i in range(n[1],n[2]) :
        r[i] += n[0]
if max(r) <= a:
    print('yes')
else:
    print('no')