z = {}
for _ in range(int(input())):
    r = []
    w = 0
    n = input()
    for i in n:
        if i not in r:
            w += 1
            r.append(i)
    if z.get(w,None) == None:
        z[w] = [n]
    else:
        z[w].append(n)
print(min(z[min(z.keys())]))