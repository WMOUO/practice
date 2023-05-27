while True:
    try:
        ans = ''
        for i in input().strip().split(' '):
            if i.isnumeric():
                ans += i

    except:
        break