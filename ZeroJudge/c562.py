while True:
    try:
        n = input()
        ans = 0
        for i in n:
            if i == '0':
                ans += 1
            elif i == '6':
                ans += 1
            elif i == '8':
                ans += 2
            elif i == '9':
                ans += 1
        print(ans)
    except:
        break