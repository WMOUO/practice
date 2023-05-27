n = input()
z = {}
for i in n:
    i = ord(i)
    if z.get(i,None) == None:
        z[i] = 1
    else:
        z[i] += 1
r = list(z.items())
r.sort(key = lambda x:(x[1],-x[0]))
for i in r:
    print(i[0],i[1])