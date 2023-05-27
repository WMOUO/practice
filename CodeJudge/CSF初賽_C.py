a,b = map(int,input().split(' '))
z = []
for _ in range(a):
    n = [int(_) for _ in input().split(' ') if _]
    z.append(n[1]//n[0])
z.sort()
r = 0
for i in z:
    if i <= b:
        r += b//i
        b -= (b//i)*i
print(r)