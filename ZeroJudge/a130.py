for t in range(1,int(input())+1):
    r = 0
    z = []
    for _ in range(10):
        n = [_ for _ in input().split(' ') if _]
        if int(n[1]) > r:
            r = int(n[1])
            z = [n[0]]
        elif int(n[1]) == r and n[0] not in z:
            z.append(n[0])
    print(f'Case #{t}:')
    for i in z:
        print(i)