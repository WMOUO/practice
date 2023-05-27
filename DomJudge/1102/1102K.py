while True:
    try:
        a = int(input())
        b = int(input())
        c = int(input())
        z = []
        while True:
            if b % 2 == 0:
                z.append(0)
            else:
                z.append(1)
            b //= 2
            if b == 1:
                break
        r = a
        while len(z) != 0:
            if z.pop() == 0:
                r = (r%c)**2
            else:
                r = ((r%c)**2)*a
        print(r%c)
        _ = input()
    except:
        break