while True:
    try:
        n = input()
        r = []
        for i in n:
            if i not in r:
                r.append(i)
        print(''.join(r))
    except:
        break