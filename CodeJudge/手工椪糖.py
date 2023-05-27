n = [_ for _ in input().split(' ') if _]
for i in range(4):
    if i == 0:
        for u in n:
            if u == 'c':
                print('  ___  ',end = '')
            elif u == 't':
                print('      ',end = '')
            elif u == 's':
                print(' _____ ',end = '')
        print()
    elif i == 1:
        for u in n:
            if u == 'c':
                print(' /   \ ',end = '')
            elif u == 't':
                print('  /\  ',end = '')
            elif u == 's':
                print('|     |',end = '')
        print()
    elif i == 2:
        for u in n:
            if u == 'c':
                print('|     |',end = '')
            elif u == 't':
                print(' /  \ ',end = '')
            elif u == 's':
                print('|     |',end = '')
        print()
    else:
        for u in n:
            if u == 'c':
                print(' \___/ ',end = '')
            elif u == 't':
                print('/____\ '[:-1],end = '')
            elif u == 's':
                print('|_____|',end = '')
        print()