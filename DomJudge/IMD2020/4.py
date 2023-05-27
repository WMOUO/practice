z = [0,1,5,8,9,10,12,17,20,24,25]
r = [0]*11
for i in range(1,len(z)):
    for u in range(10,0,-1):
        if u >= i:
            r[u] = max(r[u],r[u]+z[i],z[u])
print(r[int(input())])