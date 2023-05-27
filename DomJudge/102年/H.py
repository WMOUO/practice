for _ in range(int(input())):
    n = sorted([int(_) for _ in input().split(' ') if _])
    if n[0]+4 == n[1] and (n[0] >= 1 and n[1] <= 14 or n[0] >= 14 and n[1] <= 27 or n[0] >= 27 and n[1] <= 40 or n[0] >= 40 and n[1] <= 52) == True:
        print('同花順')
    else:
        z = {}
        for i in range(len(n)):
            n[i] = n[i] % 13
        for i in n:
            if z.get(i,None) == None:
                z[i] = 1
            else:
                z[i] += 1
        r = sorted(list(z.values()))
        w = sorted(list(z.keys()))
        if len(z) == 2:
            if r == [2,3]:
                print('葫蘆')
            else:
                print('四對')
        elif len(z) == 3:
            if r == [1,1,3]:
                print('三條')
            elif r == [1,2,2]:
                print('兩對')
        elif len(z) == 4:
            print('一對')
        else:
            if w[0] + 4 == w[-1] and (w[0] >= 1 and w[1] <= 14 or w[0] >= 14 and w[1] <= 27 or w[0] >= 27 and w[1] <= 40 or w[0] >= 40 and w[1] <= 52) == True:
                print('順子')
            else:
                print('雜牌')