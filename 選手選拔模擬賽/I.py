while True:
    a = int(input())
    if a == 0:
        break
    n = [_ for _ in input().split(' ') if _]
    for i in range(len(n)):
        if n[i][0] == 'N':
            n[i] = int(n[i][1:])*2
        else:
            n[i] = int(n[i][1:])*(-1)
    n[0] = max(0,n[0])
    for i in range(1,len(n)):
        n[i] = max(0,n[i-1]+n[i])
    if max(n) > 0:
        print(max(n))
    else:
        print('INVALID')
#6
#F99 N5 F9 N5 F5 N2
#3
#F999 N50 F9
#5
#N6 F4 F10 N2 N5
#3
#F2 F1 F2
#0