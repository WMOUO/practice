r = [0,0,0,0]
w = [0]*7
for i in range(7):
    a = 0
    for u in [eval(_) for _ in input().split(' ') if _]:
        r[a] += u
        w[i] += u
        a += 1
print(w.index(max(w))+1)
e = max(r)
if e == r[0]:
    print('morning')
elif e == r[1]:
    print('afternoon')
elif e == r[2]:
    print('night')
else:
    print('early morning')