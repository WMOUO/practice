n = int(input())
for _ in range(n) :
    L = [a for a in input().split(",") if a]
    v = int(L[0])
    f = int(L[0])
    e = int(L[1])
    i = 2
    o = 0
    z = []
    p = 0
    if len(L) == 0 :break
    while i <= v :   
        while v % i == 0:
            o += 1
            v = v // i
        if o != 0:    
            if len(z) == 0 :
                z.append(str(i))
            else:
                z.append('*')
                z.append(str(i))    
            if o > 1 :
                z.append('^')
                z.append(str(o))
        i += 1 
        o = 0 
    if v != 1 :
        z.append('*')
        z.append(str(v))
    for t in range(e,0,-1):
        if f % t == 0 and e % t == 0:
            z.append(", ")
            z.append(str(t))
            p = 1
            break
    if p == 0 :
        z.append(", ")
        z.append(str(t))
    print(''.join(z))