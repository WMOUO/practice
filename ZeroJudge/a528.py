while True:
    try:
        z = []
        for _ in range(int(input())):
            z.append(eval(input()))
        z.sort()
        for i in z:
            print(i)
    except:
        break