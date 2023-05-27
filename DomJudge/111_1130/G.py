for _ in range(int(input())):
    a = ''
    b = ''
    z = ''
    for i in input():
        if i.isnumeric():
            b += i
        else:
            if len(b) != 0:
                z += (a * int(b))
                b = ''
            a = i
    print(z+a * int(b))