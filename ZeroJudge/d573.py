while True:
    try:
        z = [0]*100001
        for i in range(1,int(input())+1):
            for u in [int(_) for _ in input().split(' ') if _][2:]:
                z[u] = i
        print(z[int(input())])
    except:
        break