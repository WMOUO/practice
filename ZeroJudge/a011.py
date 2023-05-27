while True:
    try:
        n = input().upper()
        ans = 1
        t = True
        for i in n:
            if ord(i) < 65 or ord(i) > 92:
                t = False
            else:
                if t == False:
                    t = True
                    ans += 1
        print(ans)
    except:
        break