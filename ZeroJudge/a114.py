for _ in range(int(input())):
    n = int(input())
    ans = None
    a = 2
    if n == 1:
        print('4')
        continue
    while True:
        if len(str(a**2)) == n:
            t = True
            for i in str(a**2):
                if int(i) % 2 == 0:continue
                else:
                    t = False
                    break
            if t == False:
                a += 2
                continue
            ans = a**2
            break
        a += 2
    print(ans)