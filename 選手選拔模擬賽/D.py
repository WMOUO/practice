for _ in range(int(input())):
    a,b = map(int,input().split(' '))
    n = [int(_) for _ in input().split(' ') if _]
    for _ in range(b):
        r = 0
        for i in input():
            if i == '-':
                continue
            r *= 2
            if i == 'L':
                r += 1
            else:
                r += 2
        print(n[r])