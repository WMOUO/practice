for _ in range(int(input())):
    a = input()
    n = [int(_) for _ in input().split(' ') if _]
    b = 0
    c = 0
    for i in n:
        if i % 2 == 0:
            b += 1
        else:
            c += 1
    print(min(b,c))