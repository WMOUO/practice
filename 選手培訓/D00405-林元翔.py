while True:
    L = [a for a in input().split(" ") if a]
    if len(L) == 0 : break
    a = int(L[0])
    b = int(L[1])
    z = []
    c = a // b
    d = int(a % b)
    if c != 0:
        c = str(c)
        z.append(c)
    if d >= 10 :
        i = 65 + (d - 10)
        i = str(chr(i))  
        z.append(i)
    else:
        d = str(d)
        z.append(d)
    print(''.join(z))