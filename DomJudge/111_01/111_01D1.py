while True:
    try:
        a = input().strip()
        a = ' '.join(a)
        a = a.split(' ')
        b = input().strip()
        b = ' '.join(b)
        b = b.split(' ')
        ans = ''
        for i in a:
            if i in b:
                c = b.index(i)
                b[c] = '0'
                ans += i
        ans = sorted(ans)
        print(''.join(ans))
    except:
        break