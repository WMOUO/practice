n = input()
z = {}
w = []
r = []
f = 0
q = ""
for _ in n:
    if z.get(_,"None") == "None":
        z[_] = 1
    else:
        z[_] += 1
x = z.keys()
if len(x) == 1:print(n)
for i in x :
    if z[i] % 2 != 0 :
        f += 1
        q = [i]
        if f == 2:
            print("NO SOLUTION")
            break
    w.append(i*(z[i]//2))
    r = [i*(z[i]//2)] + r
if q == '':
    ans = w + r
else:
    ans = w + q + r
print("".join(ans))