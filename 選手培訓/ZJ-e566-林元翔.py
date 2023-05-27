while True:
    try:
        n = [int(n) for n in input().split(" ") if n]
        a = n[0]
        z = [a]
        t = True
        if n[1] == 0 :
            print("Boring!")
            continue
        elif n[1] == 1:
            for i in range(n[0]-1,0,-1):
                z.append(i)
            z = list(map(str,z))
            print(" ".join(z))
            continue
        while a > 1:
            a = a // n[1]
            z.append(a)
        if t != False:
            for i in z[:-1]:
                if i % n[1] != 0:
                    t = False
                    break
        if t != False:
            z = list(map(str,z))
            print(" ".join(z))
        else:print("Boring!")
    except:
        break