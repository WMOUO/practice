def P(A):
    z = []
    x = []
    f = -1
    for i in range(1,A+1):
        i = str(i)
        z.append(i)
    while len(z) != 1:
        if len(z) == 2:
            x.append(z[0])
            z = z[1:]
        else:    
            f += 1
            x.append(z[f])
            f += 1 
            z.append(z[f])
            z=z[2:]
            f = -1
    a = ', '.join(x)
    b = z[-1]
    print(f"Discarded cards: {a}")
    print(f'Remaining card: {b}')
while True :
    try:
        L = int(input())
        if L == 0 :break
        V = P(L)
    except:
        break