n = int(input())
z = []

e = 1
y = 0
for i in range(1,n+1):
    z.append(i)
w = sum(z)
a = w / 2
if a == int(a):
    while True:
        c = []
        b = int(a)
        r = (b-e)//2
        if r in z and (r+1) in z:
            c.append(e)
            c.append(r)
            c.append(r+1)
            y += 1
            for j in c:
                if j % 2 == 0:
                    if j // 2 - 1 not in c and j // 2 + 1 not in c:
                        y += 1
                else:
                    if j // 2 not in c and j // 2 + 1 not in c:
                        y += 1
        e += 1
        if e > n // 2 :break
print(y//2)