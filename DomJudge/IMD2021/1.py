while True:
    try:
        n = input()
        z = 0
        r = -1
        t = 1
        for i in n:
            if r == -1:r = int(i)
            else:
                if int(i) >= r:
                    r = int(i)
                    t += 1
                else:
                    z = max(t,z)
                    t = 1
                    r = int(i)
        z = max(t,z)
        print(z)
    except:
        break