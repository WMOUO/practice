for _ in range(int(input())):
    a = input()
    n = [int(_) for _ in input().split(' ') if _]
    z = []
    r = 0
    for i in n:
        if i not in z:
            z.append(i)
        else:
            r += 1
    if r % 2 == 0:
        print(len(z))
    else:
        print(len(z)-1)