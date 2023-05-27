while True:
    try:
        a,b = map(int,input().split(' '))
        if b == 0:
            print('Go Kevin!!')
        else:
            if (a-1)%b == 0:
                print('Go Kevin!!')
            else:
                print('No Stop!!')
    except:
        break