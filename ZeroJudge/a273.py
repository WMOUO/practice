while True:
    try:
        n = [int(_) for _ in input().split(' ') if _]
        if n[0] == 0:
            print('Ok!')
        elif n[1] == 0:
            print('Impossib1e!')
        elif n[0] % n[1] == 0:
            print('Ok!')
        else:
            print('Impossib1e!')
    except:
        break