a = sorted([eval(_) for _ in input().split(',') if _]+[float('inf')])
b = sorted([eval(_) for _ in input().split(',') if _]+[float('inf')])
r = 0
z = 0
while len(a) != 1 and len(b) != 1:
    if a[0] < b[0] :
        a.pop(0)
        r += 1
        z = max(z,r)
    else:
        b.pop(0)
        r -= 1
print(z)