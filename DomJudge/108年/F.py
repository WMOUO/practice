for _ in range(int(input())):
    n = [int(_) for _ in input().split(' ') if _]
    r = n[0]
    ans = str(n[0]//n[1])
    r = r % n[1] * 10
    z = [r]
    ans += '.'
    while True:
        ans += str(r//n[1])
        if ans[-1] == '0' and r == 0:
            ans = ans[:-1]+'('+ans[-1]+')'
            break
        else:
            t = False
            r = r % n[1] * 10
            for i in range(len(z)):
                if z[i] == r:
                    w = ans[:i+2]
                    ans = w +'('+ans[i+2:]+')'
                    t = True
                    break
            if t == False:
                z.append(r)
                if len(z) == 51:
                    ans = ans[:2]+'('+ans[2:]+'...)'
                    break
            else:
                break
    print(ans)