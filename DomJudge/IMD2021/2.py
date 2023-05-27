while True:
    try:
        n = input()
        z = []
        for i in n:
            if i in z:z.remove(i)
            z.append(i)
        print(''.join(z))
    except:
        break