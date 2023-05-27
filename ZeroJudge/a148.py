while True:
    try:
        n = input()
        z = {}
        for i in n:
            if z.get(chr(i),"None") == "None":
                z[chr(i)] = 1
            else:
                z[chr(i)] += 1
        h = z.keys()
        for i in h:
            print(i,z[i])
    except:
        break