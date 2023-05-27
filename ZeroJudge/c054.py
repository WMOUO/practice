a = ' '.join("QWERTYUIOP[]`1234567890-=ASDFGHJKL;'ZXCVBNM,./").split(' ')
while True:
    try:
        ans = ''
        n = input()
        for i in n:
            if ord(i) == 92:
                ans += ']'
            elif i == ' ':
                ans += ' '
            else:
                ans += a[a.index(i)-1]
        print(ans)
    except:
        break